# 🎓 CampusGPT – AI Powered Campus Assistant

CampusGPT is a Flask-based AI assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions from a custom campus knowledge base (PDFs/documents).

It allows students or faculty to interact with institutional data in a conversational way.

---

## 🚀 Features

- 📂 Upload and use custom PDFs as knowledge base
- 🤖 RAG-based intelligent answer generation
- 🌐 Simple Flask Web Interface
- ⚡ Fast and lightweight
- 🎨 Clean frontend using HTML, CSS, JS

---

## 🛠️ Tech Stack

- Python
- Flask
- LangChain
- PyPDFLoader
- HTML / CSS / JavaScript
- RAG Architecture

---

## 📁 Project Structure

```
CampusGPT/
│
├── app.py
├── rag_system.py
├── requirements.txt
│
├── knowledge_base/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── env1/ (virtual environment – not required in repo)
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/CampusGPT.git
cd CampusGPT
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate:

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 📂 Add Knowledge Base

Put your PDF files inside:

```
knowledge_base/
```

---

## ▶️ Run the App

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User asks a question
2. Flask receives the request
3. RAG system retrieves relevant document chunks
4. AI generates contextual response
5. Response is displayed on the web interface

---

## 🔮 Future Enhancements

- Authentication system
- Cloud deployment
- Multi-document support improvement
- Admin dashboard
- Chat history memory

---

## 📜 License

This project is open-source and free to use.

---

## 💡 Hackathon Tagline

> Transforming static campus documents into an intelligent conversational assistant using AI.
