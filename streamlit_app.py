import streamlit as st
import tempfile
import os

st.title("อัปโหลดวิดีโอเพื่อประมวลผล")

# รับวิดีโอจากผู้ใช้
video_file = st.file_uploader("อัปโหลดไฟล์วิดีโอ (.mp4)", type=["mp4", "mov", "avi"])

if video_file is not None:
    # สร้างไฟล์ชั่วคราว
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(video_file.read())

    st.success("อัปโหลดสำเร็จ")
    st.video(tfile.name)

    # ===== ทำงานต่อกับวิดีโอนี้ได้ เช่น cv2.VideoCapture =====
    import cv2

    cap = cv2.VideoCapture(tfile.name)
    st.write("จำนวนเฟรมทั้งหมด:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

    # ปิดการใช้งาน
    cap.release()

    # ลบไฟล์หลังจากเสร็จ (ถ้าต้องการ)
    if st.button("ลบไฟล์ชั่วคราว"):
        os.remove(tfile.name)
        st.success("ลบไฟล์แล้ว")
        
import ultralytics
ultralytics.checks()
