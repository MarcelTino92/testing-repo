import streamlit as st
def simulate_ctrl_w():
    st.write("""
    <script>
    function simulateCtrlW(){
    const event=new
    keyboardEvent('keydown',{
                key: 'w'
                code: 'KeyW'
                ctrlKey: true,
             });
    document.dispatchEvent(event):
            }
    document.getElementsById('myButton').addEventListener('click',simulateCtrlW);
    <script>
    """,unsafe_allow_html=True)

st.button("Simulate Ctrl+W",on_click=simulate_ctrl_w)
