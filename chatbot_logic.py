from langchain.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents():
    docs = []
    loaders = [
        PyPDFLoader("data/vanban1.pdf"),
        Docx2txtLoader("data/vb_123.docx"),
    ]
    for loader in loaders:
        docs.extend(loader.load())
    return docs

def create_vectorstore(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    db = FAISS.from_documents(chunks, OpenAIEmbeddings())
    return db
