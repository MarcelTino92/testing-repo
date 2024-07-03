import streamlit as st

def simulate_404_page():
  """Simulates a Google-like 404 error page using Streamlit."""

  # Background image (replace with desired Google logo or background)
  st.markdown("""<body style="background-image: url('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color.png'); background-size: contain; background-repeat: no-repeat; background-position: center;">""", unsafe_allow_html=True)

  # Content area with semi-transparent overlay
  st.markdown("""<div style="background-color: rgba(255, 255, 255, 0.8); margin: 100px auto; padding: 30px; border-radius: 5px; text-align: center;">""", unsafe_allow_html=True)

  st.title("404. That's not a thing here.")
  st.write("The page you requested could not be found. It might be missing or temporarily unavailable.")

  # Search bar (optional)
  # st.markdown("""<div style="display: flex; justify-content: center;">
  #     <input type="text" style="padding: 10px 20px; border: 1px solid #ccc; border-radius: 5px; margin: 10px;">
  #     <button style="background-color: #4285f4; color: white; padding: 5px 10px; border: none; border-radius: 5px;">Search</button>
  # </div>""", unsafe_allow_html=True)

  st.markdown("</div>", unsafe_allow_html=True)  # Close content area
  st.markdown("</body>", unsafe_allow_html=True)  # Close background

simulate_404_page()
