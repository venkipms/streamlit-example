# Example 1
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(' Option for Personal contact:',
                                            ('Email', 'Landline', 'Mobile phone'))
"Personal Contact Selected: ", add_selectbox

# Add a slider to the sidebar:
add_slider = st.sidebar.slider('Select a range of values', 0, 100)
"Range Selected: ", add_slider

# Example 2
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('SUBMIT')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio('Programming Language',
        ("Python", "Java", "Kotlin", "Scala"))
    st.write(f"Language {chosen} Selected")
