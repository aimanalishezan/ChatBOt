from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#langchain tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
#creating cheat bot
prompt=ChatPromptTemplate.from_massages(
    [
        ("system","you are e helpful assistant.please provide response to the user queries"),
        ("user","Question:{question}")
    ]
)
#streamlit framework
st.title("Aiman's\n Man.AI")
input_text=st.text_input("search the topic you want")
#llm call
llm=ollama(model="llama3.2")
output_parser=StrOutputParser
#chain
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text}))