#from langchain.chat_models import ChatOpenAI
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import  add_routes
from langchain_community.llms import Ollama
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
# add_routes(
#     api,
#     #ChatOpenAI()
#     path="/openai"
# )
#open ai llm modelS
#model=ChatOpenAI()

#ollama llm model
llm=Ollama(model="llama3.2")


prompt1=ChatPromptTemplate.from_template("Write a story about {topic} with 100 words")
#prompt2=ChatPromptTemplate.from_template("Write a poem about {topic} for child")


add_routes(
    api,
    prompt1|llm,
    path="/story"
)
# add_routes(
#     api,
#     prompt2|model,
#     path="/poem"
# )

if __name__=="__main__":
    uvicorn.run(api,host="localhost",port=8000)