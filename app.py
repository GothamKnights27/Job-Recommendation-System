import streamlit as st
import pandas as pd
import time
import PyPDF2

# Importing the predict function from model.py
from model import predict 

st.title("Job Recommendation System")

uploaded_file = st.file_uploader("Upload your Resume", type='pdf')

text = "We believe these 5 jobs are a good fit for you!"

def stream_data():
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""

    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    result = predict(resume_text)

    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)

    yield pd.DataFrame(result)

if st.button("Recommend me Jobs"):
    st.write_stream(stream_data())

st.divider()

st.caption("Developed and packaged by: Saumya Karia and Kedar Dhamankar")
