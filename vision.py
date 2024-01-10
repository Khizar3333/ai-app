from dotenv import load_dotenv
import streamlit as st
load_dotenv()
from PIL import Image
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gimini_response(input,image):
 if input!="":
  response=model.generate_content([input,image])
 else:
  response=model.generate_content(image)
   
 return response.text
st.set_page_config(page_title="Gemini image demo")
st.header("Gemini LLM Application")



input=st.text_input("Input Prompt",key="input")

# make an option to upload file
uploaded_file=st.file_uploader("Upload image",type=["png","jpg","jpeg"])
image=""
if uploaded_file is not None:
 image=Image.open(uploaded_file)
 st.image(image,caption="uploaded image",use_column_width=True)


submit=st.button("tell me about this image")

if submit:
  response=get_gimini_response(input,image)
  st.subheader("the response is")
  st.write(response)



