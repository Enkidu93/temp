import streamlit as st
import subprocess

st.title("THIS IS AN EXAMPLE")
if st.button("Run subprocess & see error"):
    ret = subprocess.run("pip list", shell=True, capture_output=True, text=True)
    st.write(ret.stdout)
    ret = subprocess.run("whereis python", shell=True, capture_output=True, text=True)
    st.write(ret.stdout)
    ret = subprocess.run("which python", shell=True, capture_output=True, text=True)
    st.write(ret.stdout)
    ret = subprocess.run(
        "python -m module.script", shell=True, capture_output=True, text=True
    )
    st.write(ret.returncode)
    st.write(ret.stdout)
    st.error(ret.stderr)

st.divider()

with st.form('Run arbitrary command'):
    cmd = st.text_input('Command')
    if st.form_submit_button():
        cmd_ret = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        st.session_state.cmd_ret = cmd_ret

if 'cmd_ret' in st.session_state:
    st.write(st.session_state.cmd_ret.returncode, st.session_state.cmd_ret.stdout, st.session_state.cmd_ret.stderr)
