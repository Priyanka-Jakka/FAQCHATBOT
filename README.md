# FAQ ChatBot 🤖

A simple FAQ chatbot built with:
- **LangChain**
- **FAISS**
- **HuggingFace embeddings**
- **Groq LLM**
- **Streamlit UI**

---

## 🚀 Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/Priyanka-Jakka/FAQCHATBOT.git
cd FAQCHATBOT
```

2. **Create virtual environment(recommended)**
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Build FAISS index (first time only)**
```bash
python build_index.py
```

5. **Run Streamlit app**
```bash
streamlit run faqchatbot/ui.py
```
