import streamlit as st
import pandas as pd
import numpy as np
import os
from langchain_core.prompts import ChatPromptTemplate    
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM   # corrected import

# Define prompt properly
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request."),
    ("user", "{input_text}")
])

st.title("My First Chatbot App")

# Input field
input_text = st.text_input("Enter your question:")

# Initialize LLM
llm = OllamaLLM(model="gemma2:2b")

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Display result only if user enters text
if input_text:
    st.write(chain.invoke({"input_text": input_text}))
