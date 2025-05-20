
from langchain_openai import ChatOpenAI  
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import streamlit as st

st.title("YOUR PERSONAL CHATBOT🤖")

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model_name="deepseek/deepseek-r1:free",
    api_key="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",
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
 
