import streamlit as st
#from dotenv import apikey


st.title("Example")


name = st.text_input("Type your name here")
if st.button("print"):
    st.write("Hello," + name)






