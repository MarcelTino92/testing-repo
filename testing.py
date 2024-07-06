import streamlit as st

#def simulate_google_404():
#  """Simulates a Google 404 error page with robot using Streamlit."""

  # Background color
  #st.markdown("""<body style="background-color: #f5f5f5; font-family: Arial, sans-serif;">""", unsafe_allow_html=True)
  # Header and robot image
  #st.markdown("""<header style="display: flex; align-items: center;">
   #    <img src="https://www.google.com/images/errors/robot.png" alt="Sad robot" style="height: 250px; margin-right: 20px;">
  #<div>
    #<h1 style="font-size:25px;"><em>Your responses have been recorded</em></h1>
    #<h1 style="font-size:25px;"><em>Since the page is already redirected, Please close the Tab.</em></h1>
  #</div>
   #    </header>""", unsafe_allow_html=True)
#simulate_google_404()

#import requests
#import streamlit.components.v1 as components
#import streamlit as st
#url=f"https://www.google.com/search?igu=1&ei=&q="
#search = st.text_input("What do you want to search for?")
#components.iframe(url, height=1200)

#st.iframe(url, allowfullscreen=True)


import streamlit as st

st.title('Iframe Example')

# Google search example
st.components.v1.iframe("https://www.google.com/search?igu=1&ei=&q=streamlit", height=600)
