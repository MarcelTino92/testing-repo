import streamlit as st

import streamlit.components.v1 as components
import streamlit as st
url=f"https://www.google.com/search?igu=1&ei=&q="
#search = st.text_input("What do you want to search for?")

import requests
data = {"username": 893, "password": 893,"question":question"How are you"}
url = f"https://programmingtraining.sawtoothsoftware.com/CBV1/cgi-bin/ciwweb.pl?studyname=ChatBot_CBV1"
response = requests.get(url, params=data)
js=f'window.open("{response.url}","_blank").then(r=> window.parent.location.href);'
st_javascript(js)
