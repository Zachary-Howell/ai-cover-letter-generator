import streamlit as st
import google.generativeai as genai
import os
from pathlib import Path

genai.configure(api_key=st.secrets["api_key"])

model = genai.GenerativeModel('gemini-pro')

# Default values from files
default_resume_path = "resumeDefault.txt"
default_excited_for_path = "excitedForDefault.txt"

default_resume_text = Path(default_resume_path).read_text() if Path(default_resume_path).exists() else ""
default_excited_for = Path(default_excited_for_path).read_text() if Path(default_excited_for_path).exists() else ""

# Streamlit app elements
st.title("Cover Letter Generator")

job_title = st.text_input("Enter the job title you are applying for:")
resume_text = st.text_area("Enter your resume text:", height=200, value=default_resume_text)
job_posting_text = st.text_area("Enter the job posting text:", height=200)
excitedFor = st.text_area("Enter what you're excited for in this position", height=200, value=default_excited_for)
additional_info = st.text_input("Any additional information for the cover letter?")

prompt = f'''
Using the following info, please generate a cover letter:
Resume Text = [{resume_text}]
Job Title = [{job_title}]
Job Posting Text = [{job_posting_text}]
What I'm Excited for in this Position = [{excitedFor}]
Additional Prompting Text = [{additional_info}]
'''

if st.button("Generate Cover Letter"):
    cover_letter_text = model.generate_content(prompt)
    st.success("Cover Letter Generated!")
    st.write(cover_letter_text.text)