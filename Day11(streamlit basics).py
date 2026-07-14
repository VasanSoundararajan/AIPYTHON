import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Dynamic User Input Form",
    page_icon="📝",
    layout="wide"
)

st.title("Dynamic User Input Form")
st.write("This application demonstrates various Streamlit input widgets.")

# -------------------------
# User Input Form
# -------------------------

with st.form("user_form"):

    st.subheader("Personal Information")

    name = st.text_input("Enter your Name")

    age = st.number_input(
        "Enter Age",
        min_value=1,
        max_value=100,
        value=18
    )

    gender = st.radio(
        "Select Gender",
        ["Male", "Female", "Other"]
    )

    education = st.selectbox(
        "Highest Qualification",
        [
            "High School",
            "Diploma",
            "Bachelor's",
            "Master's",
            "PhD"
        ]
    )

    skills = st.multiselect(
        "Select Skills",
        [
            "Python",
            "Java",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "Streamlit"
        ]
    )

    experience = st.slider(
        "Years of Experience",
        0,
        20,
        1
    )

    joining_date = st.date_input(
        "Preferred Joining Date"
    )

    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    relocate = st.checkbox("Willing to Relocate")

    submitted = st.form_submit_button("Submit")

# -------------------------
# Display Results
# -------------------------

if submitted:

    st.success("Form Submitted Successfully")

    result = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Education": education,
        "Skills": ", ".join(skills),
        "Experience": experience,
        "Joining Date": joining_date,
        "Relocate": relocate
    }

    st.subheader("Collected Information")

    st.write(result)

    df = pd.DataFrame([result])

    st.dataframe(df)

    if resume is not None:

        st.info(f"Uploaded File: {resume.name}")