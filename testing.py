import streamlit as st

def simulate_expired_page():
  """Simulates a Google-like expired page using Streamlit."""

  # Background image (replace with desired Google logo or background)
  st.markdown("""<body style="background-image: url('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color.png'); background-size: contain; background-repeat: no-repeat; background-position: center;">""", unsafe_allow_html=True)

  # Content area with semi-transparent overlay
  st.markdown("""<div style="background-color: rgba(255, 255, 255, 0.8); margin: 100px auto; padding: 30px; border-radius: 5px; text-align: center;">""", unsafe_allow_html=True)

  st.title("This page has expired.")
  st.write("The content you requested is no longer available.")
  st.write("This could be due to a session timeout or the content being removed.")

  # Buttons (replace with appropriate text/links)
  st.markdown("""<div style="display: flex; justify-content: center;">
      <button style="background-color: #4285f4; color: white; padding: 10px 20px; border: none; border-radius: 5px; margin: 10px;">Search Again</button>
      <button style="background-color: #f44336; color: white; padding: 10px 20px; border: none; border-radius: 5px; margin: 10px;">Go to Google Home</button>
  </div>""", unsafe_allow_html=True)

  st.markdown("</div>", unsafe_allow_html=True)  # Close content area
  st.markdown("</body>", unsafe_allow_html=True)  # Close background

simulate_expired_page()
