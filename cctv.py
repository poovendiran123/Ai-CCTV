import streamlit as st
import subprocess
import psutil

st.title("AI CCTV Control")

if "process_pid" not in st.session_state:
    st.session_state.process_pid = None

if st.button("▶ Start CCTV"):

    if st.session_state.process_pid is None:

        process = subprocess.Popen(
            ["python", "main.py"]
        )

        st.session_state.process_pid = process.pid

        st.success("CCTV Started")

    else:
        st.warning("CCTV Already Running")


if st.button("⏹ Stop CCTV"):

    if st.session_state.process_pid:

        try:
            p = psutil.Process(
                st.session_state.process_pid
            )

            p.terminate()

            st.success("CCTV Stopped")

            st.session_state.process_pid = None

        except:
            st.error("Process Not Found")