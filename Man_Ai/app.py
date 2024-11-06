from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Verify environment variable
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
if not langchain_api_key:
    raise ValueError("LANGCHAIN_API_KEY environment variable not set.")
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Creating the chat bot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please provide responses to user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework
st.title("Aiman's Man.AI")
input_text = st.text_input("Search the topic you want")

# LLM call
llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser
if input_text:
    st.write(chain.invoke({'question': input_text}))
