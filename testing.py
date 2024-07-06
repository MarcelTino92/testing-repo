import streamlit as st

import streamlit.components.v1 as components
import streamlit as st
url=f"https://www.google.com/search?igu=1&ei=&q="
#search = st.text_input("What do you want to search for?")
components.iframe(url, height=1200)

