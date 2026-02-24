import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load model and data
model = joblib.load("models/student_model.pkl")
data = pd.read_csv("data/student_data.csv")

st.set_page_config(page_title="Academic Monitoring System", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .main {background-color: #0f172a;}
    h1 {color: #38bdf8;}
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Smart Academic Monitoring System")

# Sidebar
st.sidebar.header("🔍 Student Evaluation Panel")

selected_class = st.sidebar.selectbox(
    "Select Class",
    sorted(data["Class"].unique())
)

class_students = data[data["Class"] == selected_class]

roll_number = st.sidebar.selectbox(
    "Select Roll Number",
    class_students["RollNo"]
)

# Class Metrics
st.subheader(f"📊 Class Overview: {selected_class}")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(class_students))
col2.metric("Average Attendance", round(class_students["Attendance"].mean(), 2))
col3.metric("Average Internal Marks", round(class_students["InternalMarks"].mean(), 2))

# Grade Distribution Chart
fig = px.histogram(
    class_students,
    x="FinalGrade",
    color="FinalGrade",
    title="Grade Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Evaluate Student
student = class_students[class_students["RollNo"] == roll_number]

attendance = student["Attendance"].values[0]
study_hours = student["StudyHours"].values[0]
internal = student["InternalMarks"].values[0]
assignment = student["Assignment"].values[0]
previous = student["PreviousSem"].values[0]

input_data = [[attendance, study_hours, internal, assignment, previous]]

prediction = model.predict(input_data)[0]

st.subheader("🎯 Individual Student Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.info(f"Attendance: {attendance}%")
    st.info(f"Study Hours: {study_hours}")
    st.info(f"Internal Marks: {internal}")

with col2:
    st.info(f"Assignment Marks: {assignment}")
    st.info(f"Previous Semester: {previous}")
    st.success(f"Predicted Grade: {prediction}")

# Risk Analysis
st.subheader("⚠ Risk Analysis")

if attendance < 50:
    st.error("High Risk: Very Low Attendance")
elif study_hours < 1:
    st.warning("Moderate Risk: Low Study Hours")
else:
    st.success("Low Risk Student")

# Suggestions
st.subheader("💡 Improvement Suggestions")

suggestions = []

if attendance < 75:
    suggestions.append("Increase attendance above 75%")
if study_hours < 2:
    suggestions.append("Study at least 2 hours daily")
if internal < 60:
    suggestions.append("Improve internal test performance")

if not suggestions:
    suggestions.append("Excellent performance. Maintain consistency!")

for s in suggestions:
    st.write("• " + s)