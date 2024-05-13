import streamlit as st
import subprocess

st.title('THIS IS AN EXAMPLE')
if st.button('Run subprocess'):
    ret = subprocess.run('python script.py')
    st.write(ret.returncode)
    st.write(ret.stdout)
    st.write(ret.stderr)