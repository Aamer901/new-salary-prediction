import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import base64

# Load the model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Function to set background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to set custom styles
def set_custom_styles():
    st.markdown(
        """
        <style>
        .title-box {
            background-color: rgba(0, 0, 0, 0.7);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
        }
        h1, h2, h3, p, label {
            color: white;
        }
        .stButton>button {
            color: black;
            background-color: #ddd;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        .prediction-box {
            border: 2px solid #333;
            padding: 20px;
            border-radius: 10px;
            background-color: #f9f9f9;
            color: #333;
            font-size: 18px;
            margin-top: 20px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image and custom styles
add_bg_from_local('C:\\Users\\Lenovo\\Project of Python\\background.avif')  # Add your background image path
set_custom_styles()

# Title of the app inside the title box
st.markdown("<div class='title-box'><h1>Salary Prediction App</h1></div>", unsafe_allow_html=True)

# Input features from the user
st.write("Enter the details below to predict the salary:")

# Input fields
age = st.number_input("Age", min_value=18, max_value=65, value=25)
gender = st.selectbox("Gender", ['Male', 'Female'])
education = st.selectbox("Education Level", ['High School', 'Bachelor', 'Master', 'PhD'])

# Full job title list
job_titles = ['Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate', 'Director', 
              'Marketing Analyst', 'Product Manager', 'Sales Manager', 'Marketing Coordinator', 
              'Senior Scientist', 'Software Developer', 'HR Manager', 'Financial Analyst', 
              'Project Manager', 'Customer Service Rep', 'Operations Manager', 'Marketing Manager', 
              'Senior Engineer', 'Data Entry Clerk', 'Sales Director', 'Business Analyst', 
              'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager', 
              'Social Media Specialist', 'Software Manager', 'Junior Developer', 'Senior Consultant', 
              'Product Designer', 'CEO', 'Accountant', 'Data Scientist', 'Marketing Specialist', 
              'Technical Writer', 'HR Generalist', 'Project Engineer', 'Customer Success Rep', 
              'Sales Executive', 'UX Designer', 'Operations Director', 'Network Engineer', 
              'Administrative Assistant', 'Strategy Consultant', 'Copywriter', 'Account Manager', 
              'Director of Marketing', 'Help Desk Analyst', 'Customer Service Manager', 
              'Business Intelligence Analyst', 'Event Coordinator', 'VP of Finance', 'Graphic Designer', 
              'UX Researcher', 'Social Media Manager', 'Director of Operations', 'Senior Data Scientist', 
              'Junior Accountant', 'Digital Marketing Manager', 'IT Manager', 
              'Customer Service Representative', 'Business Development Manager', 
              'Senior Financial Analyst', 'Web Developer', 'Research Director', 
              'Technical Support Specialist', 'Creative Director', 'Senior Software Engineer', 
              'Human Resources Director', 'Content Marketing Manager', 'Technical Recruiter', 
              'Sales Representative', 'Chief Technology Officer', 'Junior Designer', 'Financial Advisor', 
              'Junior Account Manager', 'Senior Project Manager', 'Principal Scientist', 
              'Supply Chain Manager', 'Senior Marketing Manager', 'Training Specialist', 'Research Scientist', 
              'Junior Software Developer', 'Public Relations Manager', 'Operations Analyst', 
              'Product Marketing Manager', 'Senior HR Manager', 'Junior Web Developer', 
              'Senior Project Coordinator', 'Chief Data Officer', 'Digital Content Producer', 
              'IT Support Specialist', 'Senior Marketing Analyst', 'Customer Success Manager', 
              'Senior Graphic Designer', 'Software Project Manager', 'Supply Chain Analyst', 
              'Senior Business Analyst', 'Junior Marketing Analyst', 'Office Manager', 'Principal Engineer', 
              'Junior HR Generalist', 'Senior Product Manager', 'Junior Operations Analyst', 
              'Senior HR Generalist', 'Sales Operations Manager', 'Senior Software Developer', 
              'Junior Web Designer', 'Senior Training Specialist', 'Senior Research Scientist', 
              'Junior Sales Representative', 'Junior Marketing Manager', 'Junior Data Analyst', 
              'Senior Product Marketing Manager', 'Junior Business Analyst', 'Senior Sales Manager', 
              'Junior Marketing Specialist', 'Junior Project Manager', 'Senior Accountant', 
              'Director of Sales', 'Junior Recruiter', 'Senior Business Development Manager', 
              'Senior Product Designer', 'Junior Customer Support Specialist', 'Senior IT Support Specialist', 
              'Junior Financial Analyst', 'Senior Operations Manager', 'Director of Human Resources', 
              'Junior Software Engineer', 'Senior Sales Representative', 'Director of Product Management', 
              'Junior Copywriter', 'Senior Marketing Coordinator', 'Senior Human Resources Manager', 
              'Junior Business Development Associate', 'Senior Account Manager', 'Senior Researcher', 
              'Junior HR Coordinator', 'Director of Finance', 'Junior Marketing Coordinator', 
              'Junior Data Scientist', 'Senior Operations Analyst', 'Senior Human Resources Coordinator', 
              'Senior UX Designer', 'Junior Product Manager', 'Senior Marketing Specialist', 
              'Senior IT Project Manager', 'Senior Quality Assurance Analyst', 'Director of Sales and Marketing', 
              'Senior Account Executive', 'Director of Business Development', 'Junior Social Media Manager', 
              'Senior Human Resources Specialist', 'Senior Data Analyst', 'Director of Human Capital', 
              'Junior Advertising Coordinator', 'Junior UX Designer', 'Senior Marketing Director', 
              'Senior IT Consultant', 'Senior Financial Advisor', 'Junior Business Operations Analyst', 
              'Junior Social Media Specialist', 'Senior Product Development Manager', 
              'Junior Operations Manager', 'Senior Software Architect', 'Junior Research Scientist', 
              'Senior Financial Manager', 'Senior HR Specialist', 'Senior Data Engineer', 
              'Junior Operations Coordinator', 'Director of HR', 'Senior Operations Coordinator', 
              'Junior Financial Advisor', 'Director of Engineering']

# Job title dropdown
job_title = st.selectbox("Job Title", job_titles)

experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=1)

# Convert categorical variables into numerical values
gender_map = {'Male': 0, 'Female': 1}
education_map = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}

gender_value = gender_map[gender]
education_value = education_map[education]

# Create a DataFrame for prediction
data = pd.DataFrame([[age, gender_value, education_value, job_title, experience]], 
                    columns=['Age', 'Gender', 'Education', 'Job_Title', 'Experience'])

# Perform one-hot encoding for 'Job_Title' column
data_encoded = pd.get_dummies(data, columns=['Job_Title'], drop_first=True)

# Align the input data columns with the model's training data
missing_cols = set(scaler.feature_names_in_) - set(data_encoded.columns)
for col in missing_cols:
    data_encoded[col] = 0  # Add missing columns with 0

data_encoded = data_encoded[scaler.feature_names_in_]  # Reorder columns

# Scale the data
data_scaled = scaler.transform(data_encoded)

# Predict salary
if st.button("Predict Salary", key="predict"):
    prediction = model.predict(data_scaled)[0]
    st.markdown(
        f"""
        <div class="prediction-box">
            <strong>Predicted Salary:</strong> ${prediction:.2f}
        </div>
        """, unsafe_allow_html=True
    )
