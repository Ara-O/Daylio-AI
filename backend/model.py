from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from IPython.display import Markdown, display
import httpx

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

class ChatMemory:
    def __init__(self):
        self.history = []
        
    #Add a new exchange (user question and assistant answer) to memory.
    def add_to_memory(self, user_input, assistant_output):
        self.history.append(f"User: {user_input}")
        self.history.append(f"Assistant: {assistant_output}")
        
    def get_history(self):
        # Return the full context (conversation history) as a single string
        return "\n".join(self.history)
    
    def clear_history(self):
        self.history = []
        
class RagModel:
    vector_store = None
    chain = None
    chat_memory = ChatMemory()
    RAG_TEMPLATE = """
        You are a helpful assistant who keeps track of all past exchanges. Here is your conversation history
        <Conversation History>
        {history}
        </Conversation History>

        Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. These are some entries at different dates that give insight into your state of mind, memories and moods. Use direct references when necessary
        Be as specific and thorough as possible and prioritize conversation history when possible to be able to gain more context and quote the conversation history context when applicable. Act conversational but start your messages by complimenting or shedding insight on the question asked.
        The person whose entries you are reading is the same person you are chatting with, so refer to them as 'you'. Make sure the answer you are giving DIRECTLY relates to the questions asked, using and citing context/quotes when necessary 
        
        <context>
        {context}
        </context>

        Answer the following question:

        {question}
    """
    
    model = None
    
    def __init__(self):
        self.model = ChatOllama(
            model="llama3.1:8b",
        )
    
    def extract_text(self, entries):
        """
            Extracts the text from the entries CSV file and processes/cleans the data
        """
        notes_compiled = ""

        for _, entry in entries.iterrows():
            notes_compiled += f"""
            { str(entry['note']) if str(entry['note']) != "nan" else ""}
            """
            
        notes_compiled = notes_compiled.replace("<br>", ".")
        notes_compiled = notes_compiled.replace("</br>", ".")

        notes_compiled = notes_compiled.replace("<b>", ".")
        notes_compiled = notes_compiled.replace("</b>", ".")
        
        return notes_compiled
    
    
    def define_model_and_store(self, all_splits):
        """
            Defines the embedding - uses the local nomic-embedding - and chroma db
        """
        try:
            local_embeddings = OllamaEmbeddings(model="nomic-embed-text")
            vector_store = Chroma.from_texts(texts=all_splits, embedding=local_embeddings)
            return vector_store
        except httpx.ConnectError as e:
            print(f"A connection error occured: {e}. Is Ollama running? Run Ollama start if so")
            return
        except Exception as e:
            print(f"An error occurred: {e}")
            return
        
        
    def split_text(self, notes_compiled):
        """
            Uses the RecursiveCharacterTextSplitter to split the compiled notes into chunks
        """
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=20)
        all_splits = text_splitter.split_text(notes_compiled)
        return all_splits

    def define_chain(self):    
        rag_prompt = ChatPromptTemplate.from_template(self.RAG_TEMPLATE)
        self.chain = (
            RunnablePassthrough.assign(context=lambda input: format_docs(input["context"]))
            | rag_prompt
            | self.model
            | StrOutputParser()
        )

    def process_entries(self, entries):
        print("Extracting text...")
        compiled_notes = self.extract_text(entries)
        
        print("Splitting texts...")
        splits = self.split_text(compiled_notes)
        
        print("Defining vector store...")
        self.vector_store = self.define_model_and_store(splits)
    
        self.define_chain()
        print("Vector store and chain defined ")
        
    def ask_question(self, question):
        history = self.chat_memory.get_history()
        
        # Get documents related to the current question
        docs = self.vector_store.similarity_search(question, k=25)
        
        markdown_output = self.chain.invoke({"history": history, "context": docs, "question": question})
        
        # Add to the chat memory
        self.chat_memory.add_to_memory(question, markdown_output)
        
        # Return the response
        return markdown_output
        
        
    