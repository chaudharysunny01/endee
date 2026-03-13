import streamlit as st
from search import search

st.title("Semantic Search using Endee")

query = st.text_input("Enter your query")

if query:
    results = search(query)

    st.write("Top Results:")
    for r in results:
        st.write(r)