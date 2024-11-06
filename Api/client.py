import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
#ollama

def get_ollama_response(input_text):
    response =requests.post("http://localhost:8000/story/invoke",json={'input':{'topic':input_text}})
    return response.json()['output']

# Verify environment variable
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY environment variable not set.")
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# openai response
# def get_openai_response(input_text1):
#     response=requests.post("http://localhost:8000/poem/invoke",json={'input':{'topic':input_text1}}
#     return response.json()['output']['context']

st.title("langchain demo with api")
input_text=st.text_input("write a story about")
#input_text1=st.text_input("write a poem")

# openai
# if input_text1:
#     st.write(get_openai_response(input_text1))

# ollama 
if input_text:
    st.write(get_ollama_response(input_text))