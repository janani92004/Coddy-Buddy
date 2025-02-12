import google.generativeai as genai
import streamlit as st

api_key='AIzaSyCEgpFZZGIJB8BauDTb9LjDg4pzVZmM-Gw'
genai.configure(api_key=api_key)

instructions=('''You are an AI coding assistant. 
              You must only answer questions related to coding, debugging, completing the code, software development in any and all languages. 
              if the query is unrelated to coding, politely decline to answer and tell them that you are willing to help in coding alone.''')


st.title("🤖Coddy Buddy: An AI Code Helper And Reviewer") 

query=st.text_area("Ask Coddy Buddy a question!",height=150)

if st.button("Get Answer"):
    if query.strip():
        model=genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"{instructions}\n\nUser Query: {query}")
        st.subheader("🌟Reply:")
        st.write(response.text)
    else:
        st.warning("Hey, you need to ask a question.")