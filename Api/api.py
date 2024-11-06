from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import  add_routes
from langchain_community.llms import ollama
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

os.environ[""]