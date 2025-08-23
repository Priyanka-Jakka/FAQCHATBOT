# search function

from faqchatbot.indexer import load_faiss_index

class Retriever:
    def __init__(self):
        vector_db=load_faiss_index()
        self.retriever=vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    def get_retriever(self):
        return self.retriever
