import streamlit as st

def calculate_total_score(midterm, final):
    """Calculates the total score from midterm and final scores."""
    return midterm + final

st.set_page_config(page_title="โปรแกรมคำนวณคะแนนรวมนักศึกษา", layout="centered")

st.title("คำนวณคะแนนรวมนักศึกษา")
st.subheader("จากโจทย์: คะแนนรวม = คะแนนสอบกลางภาค + คะแนนสอบปลายภาค")

# Input fields
midterm_score = st.number_input(
    "1. กรุณาป้อนคะแนนสอบกลางภาค (Midterm Score):",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.5,
    key="midterm"
)

final_score = st.number_input(
    "2. กรุณาป้อนคะแนนสอบปลายภาค (Final Exam Score):",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=0.5,
    key="final"
)

# Calculation and Output
if st.button("คำนวณคะแนนรวม"):
    # Simple validation (though number_input handles min/max)
    if midterm_score < 0 or final_score < 0:
        st.error("คะแนนต้องไม่เป็นค่าลบ")
    else:
        total_score = calculate_total_score(midterm_score, final_score)
        
        st.success(f"✅ ผลการคำนวณคะแนนรวม:")
        st.metric(
            label="คะแนนรวมที่นักศึกษาได้รับ (Total Score)",
            value=f"{total_score:.2f} คะแนน"
        )
        
        st.markdown("---")
        st.info(f"**การวิเคราะห์:**")
        st.markdown(f"- **ข้อมูลนำเข้า (Input):** คะแนนสอบกลางภาค ({midterm_score}) และ คะแนนสอบปลายภาค ({final_score})")
        st.markdown(f"- **กระบวนการ (Process):** คะแนนกลางภาค + คะแนนปลายภาค = {midterm_score} + {final_score}")
        st.markdown(f"- **ข้อมูลนำออก (Output):** คะแนนรวม ({total_score})")

st.markdown("---")
st.caption("แอปพลิเคชัน Streamlit โดย Manus AI")
