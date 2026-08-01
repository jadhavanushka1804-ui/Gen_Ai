import streamlit as st
import pandas as pd
import numpy as np
st.title("My First Streamlit APP")
st.write("Hello kaveri")
st.text("Lets start")
name =st.text_input("Enter name:")
if st.button("Greet"):
     st.success(f"Hello,{name}!")
     
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)