import streamlit as st
from datetime import date

st.set_page_config(page_title="Inputs", layout="wide")
st.title("Inputs")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Text & numbers")
    name = st.text_input("text_input")
    note = st.text_area("text_area")
    n = st.number_input("number_input", value=42)
    val = st.slider("slider", 0, 100, 50)

with col2:
    st.subheader("Select")
    lang = st.selectbox("selectbox", ["Python", "Rust", "Go"])
    tags = st.multiselect("multiselect", ["A", "B", "C", "D"], default=["A"])
    choice = st.radio("radio", ["Option 1", "Option 2"], horizontal=True)
    pill = st.pills("pills", ["Fast", "Simple", "Scalable"])

with col3:
    st.subheader("Boolean & date")
    cb = st.checkbox("checkbox", value=True)
    tog = st.toggle("toggle")
    d = st.date_input("date_input", value=date.today())
    color = st.color_picker("color_picker", "#FF4B4B")
    uploaded = st.file_uploader("file_uploader")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("Regular button"):
        st.toast("Clicked!")

with col2:
    with st.form("my_form"):
        email = st.text_input("Email")
        if st.form_submit_button("Submit"):
            st.success(f"Submitted: {email}" if email else "Fill in the field")
