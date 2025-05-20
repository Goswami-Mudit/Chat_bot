
from langchain_openai import ChatOpenAI  
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import streamlit as st

st.title("YOUR PERSONAL CHATBOT🤖")

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model_name="deepseek/deepseek-r1:free",
    api_key="sk-or-v1-240e668b1fcfe173812525168b549a52d982e6ddf7452ce6d477bcc4294de9",
    temperature=0.7
)

if 'conversation' not in st.session_state:
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ask anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.spinner("Thinking..."):
        response = st.session_state.conversation.run(prompt)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
 
