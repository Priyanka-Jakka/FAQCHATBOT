# standalone script to rebuild index
from faqchatbot.indexer import build_faiss_index

if __name__ == "__main__":
    build_faiss_index()
