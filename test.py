import streamlit as st
import subprocess

st.title("THIS IS AN EXAMPLE")
if st.button("Run subprocess"):
    ret = subprocess.run("pip list", shell=True, capture_output=True, text=True)
    print(ret.stdout)
    ret = subprocess.run("which python", shell=True, capture_output=True, text=True)
    print(ret.stdout)
    ret = subprocess.run(
        "python -m module.script", shell=True, capture_output=True, text=True
    )
    print(ret.stdout)
    print(ret.stderr)
    st.write(ret.returncode)
    st.write(ret.stdout)
    st.write(ret.stderr)
