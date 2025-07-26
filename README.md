# 🧠 PA 211 Disaster Help RAG App

**A Retrieval-Augmented Generation (RAG) Streamlit app to support disaster response using PA 211 services.**

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-blueviolet)
![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📦 Features

- 🔍 Semantic search across FEMA, Ready.gov, and PA 211 docs
- 🧠 Query transformation for localized and relevant results
- 🔗 OpenAI + Gemini support for response generation
- 💬 Streamlit UI for live demo
- 📊 User feedback logging
- 🗂 Modular RAG pipeline (chunking, retrieval, generation)

---

## 🚀 How to Use (Locally)

```bash
git clone https://github.com/yourusername/pa211-disaster-rag.git
cd pa211-disaster-rag

# Install dependencies
pip install -r requirements.txt

# Step 1: Embed documents
python src/embed_documents.py

# Step 2: Launch Streamlit app
streamlit run app/streamlit_app.py
```

---

## ☁️ Deploy to Streamlit Cloud

1. Upload this repo to GitHub
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Select the repo, use `app/streamlit_app.py` as the entry point
4. Add `OPENAI_API_KEY` in Advanced Settings

---

## 🔒 Environment Variables

In Streamlit Cloud or `.env`:

```
OPENAI_API_KEY=your-openai-key
# Optional: GEMINI_API_KEY=your-gemini-key
```

---

## 📁 Directory Structure

```
📦 pa211-disaster-rag/
├── app/
│   └── streamlit_app.py
├── data/
│   └── <PDF, DOCX, RTF disaster docs>
├── embeddings/
├── logs/
├── src/
│   ├── embed_documents.py
│   ├── feedback.py
│   ├── generation.py
│   ├── query_transform.py
│   └── retrieval.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 📄 License

This project is licensed under the MIT License.