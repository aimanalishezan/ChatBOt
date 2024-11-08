import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import SystemMessagePromptTemplate,HumanMessagePromptTemplate,AIMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate


#stramlit structure
st.title("🤖 MAN.AI" )
st.write("DEVELOPER: MD AIMAN ALI SHEZAN")
llm_model=ChatOllama(model="llama3.2")
system_message=SystemMessagePromptTemplate.from_template("You are a helpful AI Assistant.You are only giving the relivant Answer.On Every correct ans you will have 200$")


if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

with st.form("input-form"):
    text=st.text_area("Enter Your Question Here")
    submit=st.form_submit_button("Submit")

def gennerate_response(chat_history):
    chat_template=ChatPromptTemplate.from_messages(chat_history)
    chain=chat_template|llm_model|StrOutputParser()
    response=chain.invoke({})
    return response

def get_history():
    chat_history=[system_message]
    for chat in st.session_state['chat_history']:
        prompt=HumanMessagePromptTemplate.from_template(chat['user'])
        chat_history.append(prompt)

        ai_message=AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.append(ai_message)
    return chat_history

if submit and text:

    with st.spinner("Gennerating Response..."):
        prompt=HumanMessagePromptTemplate.from_template(text)
        chat_history=get_history()
        chat_history.append(prompt)
        response=gennerate_response(chat_history)

        st.session_state['chat_history'].append({'user':text,'assistant':response})
        # st.write('response',response)
        # st.write(st.session_state['chat_history'])

st.write('#Chat History')
for chat in reversed( st.session_state['chat_history']):
    st.write(f"**:adult: user**:{chat['user']}")
    st.write(f"**:brain: Assistant**:{chat['assistant']}")
    st.write("---")