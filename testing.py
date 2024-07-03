import streamlit as st

st.markdown("""
<div style="
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f0f0f0;
">
    <div style="
        background-color: white;
        padding: 30px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        text-align: center;
    ">
        <h1 style="color: #dc3545;">Page Expired</h1>
        <p>The page you requested has expired. Please refresh the page to access the content again.</p>
        <button style="
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        ">Refresh</button>
    </div>
</div>
""", unsafe_allow_html=True)

