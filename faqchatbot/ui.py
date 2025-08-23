# streamlit app
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import httpx
from faqchatbot.retriever import Retriever
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()
llm=ChatGroq(
    model="gemma2-9b-it",
    temperature=0,  # ✅ Explicit key to avoid 401
    http_client=httpx.Client(verify=False)
)

retriever=Retriever().get_retriever()

template=[("system","""You are an FAQ chatbot. Answer strictly from the context.If the answwer is not present, reply with: "I don't know".
           Context:{context}"""),
          ("human", "Question: {question}")]


prompt_template=ChatPromptTemplate.from_messages(template)

def get_chain():
    return prompt_template|llm|StrOutputParser()

def answer_question(query):
    
    docs=retriever.get_relevant_documents(query)
    # print(docs)
    context = "\n\n".join([doc.page_content for doc in docs])
    chain=get_chain()
    answer=chain.invoke({"context":context,"question":query})
    
    return answer,docs

# --- Streamlit UI ---
st.set_page_config(page_title="FAQ ChatBot", layout="centered")
st.title("💬 FAQ ChatBot")

query=st.text_input("Ask me a question")

if query:
    answer,docs=answer_question(query)
    st.subheader("Answer:")
    st.write(answer)
    with st.expander("See matching FAQ entries"):
        for doc in docs:
            content_lines = doc.page_content.split("\n")
            prompt_text = content_lines[0].replace("prompt:", "").strip() if len(content_lines) > 0 else ""
            response_text = content_lines[1].replace("response:", "").strip()
            st.markdown(f"**Matched Question:** {doc.metadata.get('source', 'N/A')}")
            st.markdown(f"**Stored Answer:** {response_text}")

    

