#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import streamlit as st
# import webbrowser as wb
from urllib.parse import urlencode


def main():
    name = st.query_params.get('name', '')
    query = st.query_params.get('query', '')

    st.title(f"Hello, {name}!")
    st.write(f"Your search query is - {query}. Please give me more details about your search query:")
    
    response = st.text_area("Enter your response:")
    
    sw_url = "https://programmingtraining.sawtoothsoftware.com/CBV1/cgi-bin/ciwweb.pl?studyname=ChatBot_CBV1&Username=501&password=501"

    html_code = """
    <script type="text/javascript">
    alert('You can now close this tab.');
    </script>
    """
    # Inject JavaScript into the Streamlit app
    components.html(html_code)

    
if __name__ == "__main__":
    main()
