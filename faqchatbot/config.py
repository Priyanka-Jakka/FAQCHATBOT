# constants, env vars
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Paths
# DATA_PATH = "/Users/dileep/Desktop/FAQCHATBOT/data/faq_mental_health.csv"   # your FAQ CSV
# # DATA_PATH="/Users/dileep/Desktop/FAQCHATBOT/data/faq_mental_health.csv"
# INDEX_PATH = "/Users/dileep/Desktop/FAQCHATBOT/faiss_index"          # FAISS index directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "faq_mental_health.csv")   # FAQ CSV
INDEX_PATH = os.path.join(BASE_DIR, "..", "faiss_index")                    # FAISS index directory

# Normalize paths
DATA_PATH = os.path.normpath(DATA_PATH)
INDEX_PATH = os.path.normpath(INDEX_PATH)