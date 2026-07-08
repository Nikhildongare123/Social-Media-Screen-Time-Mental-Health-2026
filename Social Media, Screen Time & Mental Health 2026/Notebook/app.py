import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("logistic_regression_model.pkl")

# Uncomment if you saved these
# scaler = joblib.load("scaler.pkl")
# label_encoders = joblib.load("label_encoders.pkl")


st.set_page_config(
    page_title="Sleep Disorder Prediction",
    page_icon="😴",
    layout="centered"
)

st.title("😴 Sleep Disorder Prediction App")

st.write("Enter Employee Details")

# -----------------------------
# Inputs
# -----------------------------

gender = st.selectbox("Gender", ["Male", "Female"])

age = st.slider("Age", 18, 80, 30)

occupation = st.selectbox(
    "Occupation",
    [
        "Doctor",
        "Engineer",
        "Teacher",
        "Lawyer",
        "Salesperson",
        "Scientist",
        "Software Engineer",
        "Manager",
        "Nurse"
    ]
)

sleep_duration = st.slider(
    "Sleep Duration",
    4.0,
    10.0,
    7.0
)

quality_sleep = st.slider(
    "Quality of Sleep",
    1,
    10,
    7
)

physical_activity = st.slider(
    "Physical Activity Level",
    0,
    100,
    40
)

stress = st.slider(
    "Stress Level",
    1,
    10,
    5
)

bmi = st.selectbox(
    "BMI Category",
    [
        "Normal",
        "Normal Weight",
        "Overweight",
        "Obese"
    ]
)

heart_rate = st.slider(
    "Heart Rate",
    50,
    120,
    75
)

daily_steps = st.slider(
    "Daily Steps",
    1000,
    20000,
    8000
)

# -----------------------------
# Encoding
# -----------------------------

gender_map = {
    "Male":1,
    "Female":0
}

occupation_map = {
    "Doctor":0,
    "Engineer":1,
    "Teacher":2,
    "Lawyer":3,
    "Salesperson":4,
    "Scientist":5,
    "Software Engineer":6,
    "Manager":7,
    "Nurse":8
}

bmi_map = {
    "Normal":0,
    "Normal Weight":1,
    "Overweight":2,
    "Obese":3
}

input_data = pd.DataFrame({

    "Gender":[gender_map[gender]],
    "Age":[age],
    "Occupation":[occupation_map[occupation]],
    "Sleep Duration":[sleep_duration],
    "Quality of Sleep":[quality_sleep],
    "Physical Activity Level":[physical_activity],
    "Stress Level":[stress],
    "BMI Category":[bmi_map[bmi]],
    "Heart Rate":[heart_rate],
    "Daily Steps":[daily_steps]

})

# If scaler used
# input_data = scaler.transform(input_data)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("✅ Person has No Sleep Disorder")

    elif prediction == 1:
        st.warning("⚠️ Person has Insomnia")

    else:
        st.error("🚨 Person has Sleep Apnea")
