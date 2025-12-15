import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(
    page_title="PlaceReady AI",
    layout="centered",
    page_icon="🎯"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #1f2937, #020617);
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
}
.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
    color: #ffffff;
}
.hero p {
    font-size: 16px;
    color: #9ca3af;
}

.result-success {
    background: linear-gradient(90deg, #0f5132, #198754);
    padding: 15px;
    border-radius: 12px;
    color: #d1e7dd;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}
.result-danger {
    background: linear-gradient(90deg, #842029, #dc3545);
    padding: 15px;
    border-radius: 12px;
    color: #f8d7da;
    font-size: 20px;
    font-weight: bold;
    text-align: center;
}
.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- HERO HEADER (4.2 DONE) ----------------
st.markdown("""
<div class="hero">
    <h1>🎯 PlaceReady AI</h1>
    <p>AI-powered system to evaluate placement readiness</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION (4.3 DONE) ----------------
st.subheader("📥 Enter Student Details")

st.markdown("<div class='card'>", unsafe_allow_html=True)

prog = st.slider("💻 Programming Skills (0–5)", 0, 5, 2)
dsa = st.slider("🧠 DSA Skills (0–5)", 0, 5, 2)
projects = st.slider("📁 Projects (0–5)", 0, 5, 2)
internship = st.selectbox("🏢 Internship Done?", ["No", "Yes"])
cgpa = st.slider("📊 CGPA (0–10)", 0.0, 10.0, 6.5)
communication = st.slider("🗣️ Communication Skills (0–5)", 0, 5, 3)

st.markdown("</div>", unsafe_allow_html=True)

internship_val = 1 if internship == "Yes" else 0

# ---------------- BUTTON ----------------
if st.button("🚀 Check Placement Readiness"):

    student_input = np.array([[prog, dsa, projects, internship_val, cgpa, communication]])
    prediction = model.predict(student_input)

    weak_areas = []
    suggestions = []

    if prog < 3:
        weak_areas.append("Programming")
        suggestions.append("Improve programming fundamentals")

    if dsa < 3:
        weak_areas.append("DSA")
        suggestions.append("Practice DSA daily")

    if projects < 3:
        weak_areas.append("Projects")
        suggestions.append("Build more real-world projects")

    if cgpa < 7:
        weak_areas.append("CGPA")
        suggestions.append("Improve academic performance")

    if communication < 3:
        weak_areas.append("Communication")
        suggestions.append("Work on communication skills")

    st.divider()

    # ---------------- RESULT ----------------
    if prediction[0] == 1:
        st.markdown("<div class='result-success'>✅ Placement Ready</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-danger'>❌ Not Placement Ready</div>", unsafe_allow_html=True)

    # ---------------- SCORE ----------------
    score = (
        prog +
        dsa +
        projects +
        communication +
        (5 if internship_val == 1 else 0) +
        (cgpa / 10) * 5
    )

    percentage = int((score / 30) * 100)

    st.subheader("📊 Placement Readiness Score")
    st.progress(percentage)
    st.write(f"**Score:** {percentage}%")

    # ---------------- WEAK AREAS ----------------
    if weak_areas:
        st.subheader("📌 Weak Areas")
        for w in weak_areas:
            st.markdown(f"<div class='card'>🔴 {w}</div>", unsafe_allow_html=True)

    # ---------------- SUGGESTIONS ----------------
    if suggestions:
        st.subheader("💡 Suggestions")
        for s in suggestions:
            st.markdown(f"<div class='card'>✅ {s}</div>", unsafe_allow_html=True)
st.markdown("""
<hr>
<center style="color:#9ca3af; font-size:14px;">
<b>Built by Rounak Rathod</b><br>
Final Year Engineering Student | AI & Data Science <br>
© 2025 PlaceReady AI
</center>
""", unsafe_allow_html=True)

