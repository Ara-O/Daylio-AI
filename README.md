
# DaylioAI
DaylioAI is an intelligent journaling assistant designed to help users reflect on their thoughts, behavior, and emotions through insightful analysis based on journal entries. It is not associated with the Daylio company and is just a pet project so that I could talk to myself.

It offers a unique perspective on the user's emotional and psychological patterns by interpreting journal data.

![image](https://github.com/user-attachments/assets/335885fd-c640-4284-8aab-d763612e68e2)

Features:

- Local Processing: All of the processing happens locally, using the Llama3.18b model, Nomic for embedding, and so on. It can be run entirely online and only runs on your computer
- Personalized Insights: Daylio AI analyzes your journal entries and provides reflective insights into your behavior, thoughts, and emotions.
- Conversation History: The assistant remembers your past interactions, enabling it to offer responses tailored to your journaling context.
- Seamless Integration: The application integrates a frontend user interface with a backend server that processes and interprets the journal data using cutting-edge NLP models.
- Ollama Integration: The application leverages Ollama, a powerful machine learning platform, to enhance its AI capabilities and process large datasets for insightful conversations.

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
