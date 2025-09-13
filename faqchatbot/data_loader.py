# load CSV

from langchain_community.document_loaders import CSVLoader

def load_csv_data(csv_file):
    """Load FAQ CSV into LangChain Documents."""
    loader = CSVLoader(file_path=csv_file, source_column="prompt", encoding="utf-8")
    data = loader.load()
    return data

# if __name__=="__main__":
#     load_csv_data("/Users/dileep/Desktop/FAQCHATBOT/data/faqs.csv")
    
