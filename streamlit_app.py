import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title = "Certificate Generator")
col1, col2 = st.columns((1,3))

col1.image("vit_3.png", use_column_width=True)

col2.title("🎓 Certificate Generator")

#st.image("vit_3.png", width=100)
# st.title("🎓 Certificate Generator")

st.subheader("It creates PDF based on the Input")

left, right = st.columns(2)

right.markdown("**Template Used**")

right.image("template.png",width=300)

env = Environment(loader=FileSystemLoader("."), autoescape = select_autoescape())
template = env.get_template("template.html")

left.markdown("**Fill Required Data**")
form = left.form("Template_Form")
student = form.text_input("Student Name")
course = form.selectbox("Choose Course", ["Python", "Java", "Big Data", "Deep Learning"], index=0,)
grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(student=student, course=course, grade=f"{grade}/100", date=date.today().strftime("%B %d,%Y"),)
    
    pdf = pdfkit.from_string(html, False)
    st.balloons()
    
    right.success("🎉 Generated Successfully!!")
   
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name= student + ".pdf",
        mime="application/octet-stream",
    )      
