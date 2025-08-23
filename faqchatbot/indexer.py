# FAISS index build/load
import os
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from faqchatbot.data_loader import load_csv_data
from faqchatbot.embedder import get_embeddings
from faqchatbot.config import DATA_PATH, INDEX_PATH

def build_faiss_index():
    """Build FAISS index from CSV and save locally."""
    data = load_csv_data(DATA_PATH)
    embeddings = get_embeddings()
    vectordb = FAISS.from_documents(data, embeddings)
    vectordb.save_local(INDEX_PATH)
    print(f"✅ Index built and saved at {INDEX_PATH}")

def load_faiss_index():
    """Load FAISS index if exists, else build new one."""
    embeddings = get_embeddings()
    if os.path.exists(INDEX_PATH):
        vectordb = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        print("✅ Index loaded successfully.")
    else:
        print("⚠️ Index not found, building new index...")
        build_faiss_index()
        vectordb = FAISS.load_local(INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    return vectordb


# if __name__=="__main__":
#     build_faiss_index()
#     load_faiss_index()


# python -m faqchatbot.indexer