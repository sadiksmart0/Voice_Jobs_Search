from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
import os
import shutil


FILE_PATH="/Users/abubakarmuktar/Documents/Data Analyst Job Resumes/Abubakar_M_DA_Resume.pdf"
URL="https://sadiksmart0.github.io/about.html"
CHROMA_PATH="/Users/abubakarmuktar/Documents/RAG_Projects/Voice_Jobs_Search/ChromaDB"


embedding_model = OllamaEmbeddings(model="mistral:instruct")

def load_document(FILE_PATH: str) -> list:
    loader = PyPDFLoader(
        file_path=FILE_PATH,
        extract_images=True
    )
    return loader.load()


def split_document(docs: list) -> list:
    text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=0,
    length_function=len
    )
    return text_splitter.split_documents(docs)



def embed_docs(chunks: list, chroma_path: str):
    """
    Embed the document chunks and store them in a Chroma database.
    If the database already exists, load it instead of recomputing.
    """
    if os.path.exists(chroma_path):
        print(f"Chroma database found at {chroma_path}. Loading existing embeddings...")
        vector_store = Chroma(persist_directory=chroma_path, embedding_function=embedding_model)
    else:
        print(f"No Chroma database found at {chroma_path}. Creating new embeddings...")
        # Erase existing Chroma DB (if any) and persist new one
        if os.path.exists(chroma_path):
            shutil.rmtree(chroma_path)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory=chroma_path
        )
        print(f"{len(chunks)} chunks saved to {chroma_path}.")
        
    return vector_store


