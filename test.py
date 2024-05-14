import streamlit as st
import subprocess

st.title("THIS IS AN EXAMPLE")
if st.button("Run subprocess"):
    subprocess.run("pip list", shell=True, capture_output=True, text=True)
    subprocess.run("which python", shell=True, capture_output=True, text=True)
    ret = subprocess.run(
        "python -m module.script", shell=True, capture_output=True, text=True
    )
    st.write(ret.returncode)
    st.write(ret.stdout)
    st.write(ret.stderr)
