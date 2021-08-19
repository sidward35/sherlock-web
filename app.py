import streamlit as st
import subprocess

st.title('Sherlock Username Search')
username = st.text_input('Username', value='', help='Enter your username')
if st.button('Submit'):
    st.text('Searching for \''+username+'\'... (this might take a minute)')
    s = subprocess.check_output(["python", "sherlock", username])
    st.text(s.decode("utf-8"))
