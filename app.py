import streamlit as st
import streamlit.components.v1 as components
import subprocess

st.set_page_config(page_title='SUS', page_icon = 'https://user-images.githubusercontent.com/27065646/53551960-ae4dff80-3b3a-11e9-9075-cef786c69364.png')
st.title('Sherlock Username Search')
username = st.text_input('Username', value='', help='Enter your username')
if st.button('Submit'):
    st.text('Searching for \''+username+'\'... (this might take a minute)')
    s = subprocess.check_output(["python", "sherlock", username])
    st.text(s.decode("utf-8"))
