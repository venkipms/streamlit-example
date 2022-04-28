# https://raw.githubusercontent.com/omnidan/node-emoji/master/lib/emoji.json

import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

col1, col2 = st.columns((1,4))

col1.image("vit_3.png", use_column_width='auto')

col2.title("HR - Order Generator")

st.subheader("Generates Faculty & Staff Probation/Confirmation Order")

left, right = st.columns(2)

right.markdown("**Template Used**")

right.image("template.png",width=350)

env = Environment(loader=FileSystemLoader("."), autoescape = select_autoescape())
template = env.get_template("template.html")

left.markdown("**Fill Required Data**")
form = left.form("Employee_Form")
emp_ID = form.text_input("Employee ID")
salutation = form.selectbox("Salutation", ["Dr.", "Mr.", "Ms.", "Mrs."], index=0,)
emp_Name = form.text_input("Employee Name")
school = form.text_input("School")
submit = form.form_submit_button(" Generate Order")

if submit:
    html = template.render(student=student, course=course, grade=f"{grade}/100", date=date.today().strftime("%B %d,%Y"),)
    
    pdf = pdfkit.from_string(html, False)
    st.balloons()
    
    right.success("🎉 Generated Successfully!!")
   
    right.download_button(
        "⬇️ Download Certificate",
        data=pdf,
        file_name= student + ".pdf",
        mime="application/octet-stream",
    )      
