# constants, env vars
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


# Paths
# DATA_PATH = "/Users/dileep/Desktop/FAQCHATBOT/data/faqs.csv"   # your FAQ CSV
DATA_PATH = "/Users/dileep/Desktop/FAQCHATBOT/data/faq_mental_health.csv"   # your FAQ CSV
# DATA_PATH="/Users/dileep/Desktop/FAQCHATBOT/data/faq_mental_health.csv"
INDEX_PATH = "/Users/dileep/Desktop/FAQCHATBOT/faiss_index"          # FAISS index directory
