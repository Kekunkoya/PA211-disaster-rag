import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from src.query_transform import enrich_query
from src.retrieval import retrieve_with_fallback
from src.generation import generate_answer
from src.feedback import log_feedback

st.set_page_config(page_title="PA 211 Disaster Help", layout="wide")
st.title("📍 PA 211 Disaster Assistance Chat")

query = st.text_input("💬 Ask your disaster-related question:")
zip_code = st.text_input("📍 Enter your ZIP code", value="17104")

if st.button("Get Help"):
    with st.spinner("Searching PA 211..."):
        enriched = enrich_query(query, zip_code)
        vs = FAISS.load_local("embeddings/pa211_faiss_index", OpenAIEmbeddings())
        docs, fallback = retrieve_with_fallback(enriched, vs)
        response = generate_answer(enriched, docs, fallback=fallback)
        st.success("✅ Answer:")
        st.write(response)

        # Feedback section
        st.markdown("#### 💬 Feedback")
        user_feedback = st.text_input("Was this helpful? Tell us more:")
        if st.button("Submit Feedback"):
            path = log_feedback(query, response, user_feedback, zip_code)
            st.success(f"Feedback saved to {path}")