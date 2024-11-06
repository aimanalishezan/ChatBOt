#from langchain.chat_models import ChatOpenAI
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import  add_routes
from langchain_community.llms import ollama
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()#for loading env variables
#set open key
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

#create the api with fastapi
api=FastAPI(

    title="langchain Server",
    version="1.0",
    description="A simple API server"
)
add_routes(
    api,
    #ChatOpenAI()
)