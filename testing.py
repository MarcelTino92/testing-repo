import streamlit as st
from streamlit_javascript import st_javascript
import streamlit.components.v1 as components
import streamlit as st
#url=f"https://www.google.com/search?igu=1&ei=&q="
#components.iframe(url, height=1200,scrolling=False)

import requests
data = {"username": 893, "password": 893,"question":"How are you"}
url = f"https://programmingtraining.sawtoothsoftware.com/CBV1/cgi-bin/ciwweb.pl?studyname=ChatBot_CBV1"
response = requests.get(url, params=data)
js1=f"window.parent.location.href = {response.url},true;"
st_javascript(js1)
#js=f'window.open("{response.url}","_blank").then(r=> window.parent.location.href);'
#st_javascript(js)
