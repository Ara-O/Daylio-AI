from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

# Handles the memory of the conversation history
class ChatMemory:
    def __init__(self):
        self.history = []
        
    #Add a new exchange (user question and assistant answer) to memory.
    def add_to_memory(self, user_input, assistant_output):
        self.history.append(f"User: {user_input}")
        self.history.append(f"Assistant: {assistant_output}")
        
    def get_context(self):
        # Return the full context (conversation history) as a single string
        return "\n".join(self.history)
    
    def clear_context(self):
        self.history = []



def extract_text(entries):
    """
        Extracts the text from the entries CSV file and processes/cleans the data
    """
    
    notes_compiled = ""

    #full_date,date,weekday,time,mood,activities,note_title,note

    for idx, entry in entries.iterrows():
        notes_compiled += f"""
        { str(entry['note']) if str(entry['note']) != "nan" else ""}
        """
        
    notes_compiled = notes_compiled.replace("<br>", ".")
    notes_compiled = notes_compiled.replace("</br>", ".")

    notes_compiled = notes_compiled.replace("<b>", ".")
    notes_compiled = notes_compiled.replace("</b>", ".")
    
    return notes_compiled
        

def split_text(notes_compiled):
    """
        Uses the RecursiveCharacterTextSplitter to split the compiled notes into chunks
    """
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=20)
    
    all_splits = text_splitter.split_text(notes_compiled)
    
    return all_splits


def define_model_and_store(all_splits):
    """
        Defines the embedding - uses the local nomic-embedding - and chroma db
    """
    
    local_embeddings = OllamaEmbeddings(model="nomic-embed-text")

    vectorstore = Chroma.from_texts(texts=all_splits, embedding=local_embeddings)
    
    return vectorstore

    
def process_file(entries):
    print("Extracting text...")
    compiled_notes = extract_text(entries)
    
    print("Splitting texts")
    splits = split_text(compiled_notes)
    
    print("Defining vector store")
    vector_store = define_model_and_store(splits)