from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
def get_gimini_response(question):
 response=model.generate_content(question)
 return response.text

# initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
input=st.text_input("input: ",key="input") 
submit=st.button("Ask a question")


if submit:
 response=get_gimini_response(input)
 st.write(response)

   
   