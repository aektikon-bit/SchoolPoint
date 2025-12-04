import streamlit as st
import pandas as pd

st.set_page_config(page_title="ระบบคำนวณคะแนนนักศึกษา", layout="centered")
st.title("🎓 ระบบคำนวณคะแนนนักศึกษา")

# ฟังก์ชันคำนวณเกรด
def calculate_grade(total):
    if total >= 80:
        return "A"
    elif total >= 75:
        return "B+"
    elif total >= 70:
        return "B"
    elif total >= 65:
        return "C+"
    elif total >= 60:
        return "C"
    elif total >= 55:
        return "D+"
    elif total >= 50:
        return "D"
    else:
        return "F"

# ข้อมูลนักศึกษาจะเก็บใน session_state
if "students" not in st.session_state:
    st.session_state.students = []

# Input ข้อมูลทีละคน
st.subheader("เพิ่มข้อมูลนักศึกษา")

name = st.text_input("ชื่อนักศึกษา")
mid = st.number_input("คะแนนกลางภาค (เต็ม 30)", min_value=0.0, max_value=30.0, step=0.5)
final = st.number_input("คะแนนปลายภาค (เต็ม 70)", min_value=0.0, max_value=70.0, step=0.5)

if st.button("เพิ่มนักศึกษา"):
    total = mid + final
    grade = calculate_grade(total)

    st.session_state.students.append({
        "ชื่อ": name,
        "กลางภาค": mid,
        "ปลายภาค": final,
        "คะแนนรวม": total,
        "เกรด": grade
    })
    st.success(f"เพิ่มข้อมูลของ {name} เรียบร้อยแล้ว!")

# แสดงผลตาราง
st.subheader("📋 ผลการคำนวณคะแนน")
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.dataframe(df, use_container_width=True)
else:
    st.info("ยังไม่มีข้อมูลนักศึกษา กรุณากรอกข้อมูลด้านบน")

# ปุ่มล้างข้อมูล
if st.button("ล้างข้อมูลทั้งหมด"):
    st.session_state.students = []
    st.warning("ล้างข้อมูลทั้งหมดแล้ว")
