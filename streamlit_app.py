import streamlit as st

st.title("ทดสอบ Streamlit Cloud")
st.write("แอปนี้รันบน Streamlit Community Cloud ผ่าน GitHub")

name = st.text_input("ชื่อของคุณคืออะไร?")
if name:
    st.success(f"สวัสดี {name}!")

