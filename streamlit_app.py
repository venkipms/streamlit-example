import streamlit as st

st.text_input("Name", key="name")
st.text_input("Age", key='age')
st.text_input("University", key='univ')

# You can access the value at any point with:
st.session_state.name
st.session_state.age
st.session_state.univ


