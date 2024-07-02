#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import streamlit as st
# import webbrowser as wb
from urllib.parse import urlencode
import streamlit.components.v1 as components

def main():
    name = st.query_params.get('name', '')
    query = st.query_params.get('query', '')

    st.title(f"Hello, {name}!")
    st.write(f"Your search query is - {query}. Please give me more details about your search query:")
    
    response = st.text_area("Enter your response:")
    
    sw_url = "https://programmingtraining.sawtoothsoftware.com/CBV1/cgi-bin/ciwweb.pl?studyname=ChatBot_CBV1&Username=501&password=501"

    st.write(f'''
    <a target="_self" href="https://programmingtraining.sawtoothsoftware.com/CBV1/cgi-bin/ciwweb.pl?studyname=ChatBot_CBV1&Username=501&password=501">
        <button>
            Submit
        </button>
    </a>
    ''',
    unsafe_allow_html=True
     )


    
if __name__ == "__main__":
    main()
