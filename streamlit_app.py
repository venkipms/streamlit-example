import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('SUBMIT')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio('Programming Language',
        ("Python", "Java", "Kotlin", "Scala"))
    st.write(f"Language {chosen} Selected")
