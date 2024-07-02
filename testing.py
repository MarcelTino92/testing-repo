import streamlit as st
import requests
data = {"username": 1, "password": 2,"question":3}
url = f"https://programmingtraining.sawtoothsoftware.com/CTDEMOCHI_V1/cgi-bin/ciwweb.pl?studyname=CTDEMOCHI_V1&sys_skipto=D1PostText&transaction_id=5&CT-1&hid_pagenum=1&hid_link=1&hid_javascript=1&hid_screenwidth=1488/embed=True"
response = requests.get(url, params=data)

res_id= f"{st.query_params.respondent}"
username=f"{st.query_params.username}"
password=f"{st.query_params.password}"
question=f"{st.query_params.question}"
st.write(f'''
    <a target="_self" href="https://programmingtraining.sawtoothsoftware.com/CBV1/cgi-bin/ciwweb.pl?studyname=ChatBot_CBV1&Username=501&password=501">
        <button>
            Submit
        </button>
    </a>
    ''',
    unsafe_allow_html=True
     )
