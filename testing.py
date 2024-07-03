import streamlit as st

def simulate_google_404():
  """Simulates a Google 404 error page with robot using Streamlit."""

  # Background color
  st.markdown("""<body style="background-color: #f5f5f5; font-family: Arial, sans-serif;">""", unsafe_allow_html=True)

  # Header and robot image
  st.markdown("""<header style="display: flex; justify-content: center; margin: 50px 0;">
      <img src="https://www.google.com/images/errors/robot.png" alt="Sad robot" style="height: 300px;">
      <h1>The Page you have used has expired. Please close this tab</h1>
  </header>""", unsafe_allow_html=True)

  # Message
  st.markdown("""<p style="text-align: center; font-size: 16px;">The requested URL /<span style="color: #607D8B;">your_url_here</span> was not found on this server. That's all we know.</p>""", unsafe_allow_html=True)

  # Search bar (optional, comment out if not desired)
  # st.markdown("""<div style="display: flex; justify-content: center; margin: 20px 0;">
  #     <input type="text" placeholder="Search Google web" style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 300px;">
  #     <button style="background-color: #4285f4; color: white; padding: 10px 20px; border: none; border-radius: 5px;">Search</button>
  # </div>""", unsafe_allow_html=True)

  st.markdown("</body>", unsafe_allow_html=True)

simulate_google_404()
