# optional setup script to make package installable
from setuptools import setup, find_packages

setup(
    name="faqchatbot",
    version="0.1.0",
    description="A simple FAQ chatbot using FAISS, HuggingFace embeddings, and Groq LLM",
    author="Priyanka",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "langchain",
        "langchain-community",
        "langchain-huggingface",
        "langchain-groq",
        "faiss-cpu",
        "pandas",
        "httpx",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)
