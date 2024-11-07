import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
#ollama

def get_ollama_response(input_text):
    try:
        #response = requests.post("http://localhost:8000/story/invoke", json={'topic': input_text})

        response = requests.post("http://localhost:8000/story/invoke/invoke?config_hash=%22A%20simple%20API%20server%22", json={'input':{'topic': input_text}})
                                                                                
        
        # Check if the request was successful
        if response.status_code == 200:
            # Attempt to parse JSON
            return response.json().get('output', 'No output received from server.')
        else:
            # Handle non-200 responses with an error message
            return f"Error: Received status code {response.status_code} from server."
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"
    except ValueError:
        # Handle JSON decoding errors
        return "Error: Failed to decode JSON response from server."
    
# def get_ollama_response(input_text):
#     response =requests.post("http://localhost:8000/story/invoke",json={'input':{'topic':input_text}})
#     return response.json().get('output',"no output")

# Verify environment variable
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY environment variable not set.")


#os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"


# openai response
# def get_openai_response(input_text1):
#     response=requests.post("http://localhost:8000/poem/invoke",json={'input':{'topic':input_text1}})
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