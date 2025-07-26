from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, UnstructuredRTFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Ensure OpenAI API Key is set
assert os.getenv("OPENAI_API_KEY"), "Please set your OPENAI_API_KEY environment variable"

pdf_paths = [
    "data/Power+Outage-English.pdf",
    "data/ready.gov_disabilities_bookmark_front-back.pdf",
    "data/ready.gov_novel-pandemic_hazard-info-sheet.pdf",
    "data/ready-gov_disaster-preparedness-guide-for-older-adults.pdf",
    "data/fema_npd_developing-and-maintaining-emergency_052125.pdf",
    "data/fema_flood-hazard-info-sheet.pdf"
]
docx_paths = ["data/Disaster Info.docx"]
rtf_paths = ["data/PA 211 Dsaster Help Overview.rtf"]

splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
chunks = []

for path in pdf_paths:
    for doc in PyPDFLoader(path).load():
        chunks.extend(splitter.split_text(doc.page_content))

for path in docx_paths:
    for doc in UnstructuredWordDocumentLoader(path).load():
        chunks.extend(splitter.split_text(doc.page_content))

for path in rtf_paths:
    for doc in UnstructuredRTFLoader(path).load():
        chunks.extend(splitter.split_text(doc.page_content))

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(chunks, embeddings)
vectorstore.save_local("embeddings/pa211_faiss_index")

print("✅ Embeddings saved.")