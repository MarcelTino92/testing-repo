import streamlit as st

def simulate_google_404():
  """Simulates a Google 404 error page with robot using Streamlit."""

  # Background color
  st.markdown("""<body style="background-color: #f5f5f5; font-family: Arial, sans-serif;">""", unsafe_allow_html=True)
  # Header and robot image
  st.markdown("""<header style="display: flex; align-items: center;">
       <img src="https://www.google.com/images/errors/robot.png" alt="Sad robot" style="height: 250px; margin-right: 20px;">
  <div>
    <h1 style="font-size:25px;"><em>Your responses have been recorded</em></h1>
    <h1 style="font-size:25px;"><em>Since the page is already redirected, Please close the Tab.</em></h1>
  </div>
       </header>""", unsafe_allow_html=True)
simulate_google_404()
