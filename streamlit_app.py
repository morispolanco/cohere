import streamlit as st
import cohere 

co = cohere.Client('KDhsUSaH5D01hlEWHEOfZvNhowIGPZC2cUcCP1sO')

st.title("Leyes de Guatemala")

question = st.text_input("Escribe tu pregunta:")

if st.button("Responder"):

  response = co.chat(
    model='command',
    message=question,
    temperature=0.3,
    chat_history=[
      {"role": "User", "message": question}
    ],
    prompt_truncation='AUTO',
    stream=True,
    citation_quality='accurate',
    connectors=[{"id":"web-search"}], 
    documents=[]
  )

  st.write("Respuesta:")
  st.write(response)
