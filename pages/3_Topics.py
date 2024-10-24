import streamlit as st

st.image("assets/logo_finstory_symboltext.png", width=100)

tab1, tab2, tab3 = st.tabs(["Business", "Sport", "Family"])

with tab1:
    st.title('Intro Business')
    st.write("")
    st.subheader("Section 1", divider="red")

with tab2:
    st.title('Intro Sport')
    st.write("")
    st.subheader("Section 1", divider="red")

with tab3:
    st.title('Intro Family')
    st.write("")
    st.subheader("Section 1", divider="red")