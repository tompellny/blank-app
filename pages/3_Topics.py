import streamlit as st

tab1, tab2 = st.tabs(["Business", "Sport", "Family"])

tab1.write("this is tab 1")

tab2.write("this is tab 2")