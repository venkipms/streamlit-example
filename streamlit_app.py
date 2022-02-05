import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(' Option for Personal contact:',
                                            ('Email', 'Landline', 'Mobile phone'))
"Personal Contact Selected: ", add_selectbox

# Add a slider to the sidebar:
add_slider = st.sidebar.slider('Select a range of values', 0.0, 100.0)
"Range Selected: ", add_slider
