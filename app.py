import streamlit as st
from PyPDF2 import PdfReader
import openai

# API Key from secrets
openai.api_key = "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"

st.title("📄 AI Document Q&A System")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.success("PDF loaded successfully!")

    question = st.text_input("Ask a question from document:")
    if question:
        st.write("### Answer:")

        sentences = text.split(".")
        result = ""

        for sentence in sentences:
            if any(word in sentence.lower() for word in question.lower().split()):
                result += sentence + ". "

        if result:
            st.write(result[:500])
        else:
            st.write("Not available in document")