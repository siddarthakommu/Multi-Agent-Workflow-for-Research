import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from agents.research_agent import retrieve_papers
from rag.chunking import chunk_text
from rag.retrieval import build_vector_store, hybrid_retrieve
from agents.summarization_agent import summarize_documents
from agents.critic_agent import critique_summaries
from agents.writer_agent import compile_final_report
from utils.logger import logger

def run_research_workflow(query):
    logger.info("=== STARTING RESEARCH WORKFLOW ===")
    papers = retrieve_papers(query)
    all_chunks = []
    for paper in papers:
        chunks = chunk_text(paper)
        all_chunks.extend(chunks)
    vector_db = build_vector_store(all_chunks)
    relevant_docs = hybrid_retrieve(query, vector_db, top_k=5)
    summaries = summarize_documents([doc.page_content for doc in relevant_docs])
    critiques = critique_summaries(summaries)
    report = compile_final_report(summaries, critiques)
    logger.info("=== WORKFLOW COMPLETED ===")
    return report

# Streamlit UI
st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🔍 AI-Powered Research Assistant")

query = st.text_input("Enter your research topic", placeholder="e.g. gaming, LLMs, cancer detection")

if st.button("Generate Report") and query.strip():
    with st.spinner("Running research workflow..."):
        try:
            final_report = run_research_workflow(query)
            st.subheader("📄 Final Report")
            st.markdown(final_report)
        except Exception as e:
            st.error(f"An error occurred: {e}")
