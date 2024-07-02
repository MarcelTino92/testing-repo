import streamlit as st
import streamlit.components.v1 as components

# Define the URL you want to allow

# Create the HTML for CSP and iframe
html_code = f"""
    <<script>
        // Define the URL to open
        var urlToOpen = "https://copilot.microsoft.com";
        <button onclick="frames[0].location.href = 'https://google.com'">Click me</button>
        // Open a new window with the specified URL
        #window.open(urlToOpen, "_self");
    </script>
"""

# Display the HTML code
components.html(html_code, height=650)
