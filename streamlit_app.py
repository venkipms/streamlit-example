import streamlit as st

X = st.slider('x')  # It's a widget
st.write(X, 'Squared Value', X * X)
