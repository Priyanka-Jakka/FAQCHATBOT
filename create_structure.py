from pathlib import Path

# Define the folder structure and initial files
structure = {
    "faqchatbot/__init__.py": "",
    "faqchatbot/config.py": "# constants, env vars\n",
    "faqchatbot/data_loader.py": "# load CSV, preprocess\n",
    "faqchatbot/embedder.py": "# embedding model logic\n",
    "faqchatbot/indexer.py": "# FAISS index build/load\n",
    "faqchatbot/retriever.py": "# search function\n",
    "faqchatbot/ui.py": "# streamlit app\n",
    "scripts/build_index.py": "# standalone script to rebuild index\n",
    "faiss_index/.gitkeep": "",
    "requirements.txt": "",
    "README.md": "# FAQChatBot\n",
    ".gitignore": "__pycache__/\n*.pyc\n.venv/\n",
    "setup.py": "# optional setup script to make package installable\n",
}

def create_project():
    root = Path.cwd()
    print(f"Creating structure under: {root}")

    for filepath, content in structure.items():
        file_path = root / filepath
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            file_path.write_text(content, encoding="utf-8")
            print(f"Created {file_path}")
        else:
            print(f"Skipped {file_path} (already exists)")

if __name__ == "__main__":
    create_project()
    print("\n✅ Project structure created.")
# This script creates the initial folder structure and files for the FAQChatBot project.