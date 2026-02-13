import os
from dotenv import load_dotenv

# Corrected imports as per LangChain's new structure
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

load_dotenv()
# Correctly reads the API key from the environment variable named "OPENAI_API_KEY"
OPENAI_API_KEY = "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"


class RAGSystem:
    def __init__(self, kb_directory):
        # A vital check to ensure the key was loaded successfully
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

        self.kb_directory = kb_directory
        # Use 'api_key' instead of the deprecated 'openai_api_key'
        self.llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
        self.vector_db = self.load_knowledge_base()
        if self.vector_db:
            print("Knowledge base loaded and indexed.")
        else:
            print("No knowledge base loaded.")

    def load_knowledge_base(self):
        documents = []
        for filename in os.listdir(self.kb_directory):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.kb_directory, filename)
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())

        if not documents:
            return None

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_documents(documents)

        # Use 'api_key' instead of the deprecated 'openai_api_key'
        embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

        vector_db = Chroma.from_documents(chunks, embeddings)
        return vector_db

    def generate_answer(self, query):
        if not self.vector_db:
            return "Knowledge base not yet configured. Please add PDF documents to the 'knowledge_base' folder."

        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever(),
            return_source_documents=True
        )

        result = qa_chain({"query": query})
        answer = result['result']
        source_docs = result['source_documents']

        if source_docs:
            source_info = f"\n(Source: {source_docs[0].metadata['source']})"
            return answer + source_info

        return answer
