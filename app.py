from flask import Flask, request, jsonify, render_template
import os
from rag_system import RAGSystem
from langchain_community.document_loaders import PyPDFLoader

app = Flask(__name__)

# Check for existence of knowledge_base directory and populate it
knowledge_base_dir = 'knowledge_base'
if not os.path.exists(knowledge_base_dir):
    os.makedirs(knowledge_base_dir)

# Initialize the RAG system
rag_system = RAGSystem(knowledge_base_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': 'Please type a message.'})
    
    bot_response = rag_system.generate_answer(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)