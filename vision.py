from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai  as genai

from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")


def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
        
    else:
        response=model.generate_content(image)    
    return response.text    
        
        
        
st.set_page_config(page_title="Gemini Image Demo") 
st.header("GEMINI Q&A LLM application")
input=st.text_input("Input Prompt",key="input")

upload_file=st.file_uploader("Choose a Image",type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image",use_column_width=True) 
    
    
    
submit=st.button("Tell me About The Image")

if submit:
    response=get_gemini_response(input,image)

    st.subheader("The response is")
    st.write(response)          