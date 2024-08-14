import os
import sys

# Add the project root to sys.path
project_root ="D:\\Data Science\\NLP\\guided project\\guided p3\\rag"
# ensure the project root is at the top of  sys.path
sys.path.insert(0, project_root)
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from custom_logger import logger  # type: ignore
from custom_exception import CustomException

def load_documents(file_path: str):
    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        logger.info(f"Documents loaded successfully from {file_path}")
        return documents
    except Exception as e:
        raise CustomException(e, sys)

def split_documents(documents: list, chunk_size: int = 2000, chunk_overlap: int = 400):
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = text_splitter.split_documents(documents)
        logger.info("Documents split into chunks successfully")
        return texts
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    file_path = os.path.join("data", "sample.pdf")
    documents = load_documents(file_path)
    texts = split_documents(documents)
