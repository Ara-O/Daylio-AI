
# DaylioAI
DaylioAI is a journaling assistant designed to help users reflect on their thoughts, behavior, and emotions. It analyzes journal entries and provides a chat interface where users can interact with their memories, and ask questions about their pasts, habits, behavioral patterns, and so on. It is not associated with the actual Daylio company/app and is just a pet project so that I could talk to myself.

![image](https://github.com/user-attachments/assets/335885fd-c640-4284-8aab-d763612e68e2)

Features:

- Local Processing: All of the processing happens locally, using the Llama3.1:8b model, Nomic for embedding, and so on. It runs entirely offline and runs only on your computer - so no one can snoop on your entries.
- Personalized Insights: Daylio AI analyzes your journal entries and provides reflective insights into your behavior, thoughts, and emotions.
- Different Modes: For larger journal entries, RAG mode can be enabled to make data-fetching more streamlined, faster and more relevant to the question - it also allows the entries to be within the context window of Llama3.1:8b. Full Context Mode takes the users entire journal into account, and allows the LLM to have a more well-rounded view of the user.
- Easy-to-use UI

### Getting Started
Prerequisites:

    Node.js: Required to run the frontend application (UI).
    Python: Required to run the backend server.
    Ollama: A machine learning platform for advanced NLP tasks.

### Installation:

    Clone this repository to your local machine.

    Navigate to the project directory and install the required dependencies for both frontend and backend.
    
#### Frontend:

    cd ui
    npm install

#### Backend:

    cd backend
    pip install -r requirements.txt

    # Steps to Process your Daylio entries
    Step through data_cleaner.ipynb 

#### Ollama
    ollama start

---

#### Alternative (Using Makefile)
To start the full application (frontend, backend, and Ollama):

    make


#### Contributing:

I welcome contributions to improve the project! If you have suggestions, improvements, or bug fixes, feel free to fork the repository and submit a pull request.

#### License:

No licenses :(

Let me know if you want any more specific details added or adjusted!
