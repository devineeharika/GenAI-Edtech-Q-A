import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

# Set page configuration
st.set_page_config(page_title="EDTECH Q&A 🌱", layout="wide")

# Sidebar for additional options
with st.sidebar:
    st.header("Options")
    if st.button("Create Knowledgebase"):
        create_vector_db()
        st.success("Knowledgebase created successfully!")
    st.markdown("## About")
    st.write("This application helps answer questions using a custom knowledge base for EDTECH.")

# Main title
st.title("EDTECH Q&A 🌱")

# Main content layout with columns
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://www.example.com/logo.png", width=150)  # Add your logo or image

with col2:
    question = st.text_input("Ask your question:")

    if question:
        with st.spinner("Generating answer..."):
            chain = get_qa_chain()
            response = chain(question)

        st.header("Answer")
        st.write(response["result"])

# Footer
st.markdown("---")
st.write("© 2024 EDTECH. All rights reserved.")
