import pickle
import streamlit as st

# Load the saved model
covid19 = pickle.load(open('covid19_model.sav', 'rb'))

# Apply styles
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://raw.githubusercontent.com/SHAIK-RAIYAN-2022-CSE/malaria/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }
    .block-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border: 2px solid #ccc;
        border-radius: 15px;
        max-width: 800px;
        margin: auto;
        backdrop-filter: blur(10px);
        box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.7);
    }
    h1 {
        color: #FF6347;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #ccc;
        color: white;
        font-size: 20px;
        padding: 12px 30px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        background-color: white;
        color: #FF6347;
        border: 2px solid #FF6347;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }
    input[type="text"], input[type="number"], select {
        background-color: white !important;
        color: black !important;
        border: 2px solid #FF6347;
        border-radius: 5px;
        padding: 12px;
        width: 100%;
        max-width: 250px;
        box-sizing: border-box;
        transition: border-color 0.3s, box-shadow 0.3s;
    }
    input[type="text"]:focus, input[type="number"]:focus, select:focus {
        border-color: #FF4500;
        box-shadow: 0 0 5px rgba(255, 99, 71, 0.5);
        outline: none;
    }
    label {
        color: white;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title with emoji
st.markdown("<h1>🌍 Covid 19 Prediction using ML 🦠</h1>", unsafe_allow_html=True)

# Getting the input data from the user
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Fever = st.text_input('🌡️ Fever')

with col2:
    Cough = st.text_input('🤧 Cough')

with col3:
    Shortness_of_Breath = st.text_input('💨 Shortness of Breath')

with col4:
    Fatigue = st.text_input('😩 Fatigue')

with col5:
    Loss_of_Taste_or_Smell = st.text_input('👅 Loss of Taste or Smell')

with col1:
    Sore_Throat = st.text_input('🤒 Sore Throat')

with col2:
    Headache = st.text_input('💥 Headache')

with col3:
    Muscle_Pain = st.text_input('💪 Muscle Pain')

with col4:
    Diarrhea = st.text_input('💩 Diarrhea')

with col5:
    Nausea = st.text_input('🤢 Nausea')

with col1:
    Chest_Pain = st.text_input('❤️ Chest Pain')

with col2:
    High_Blood_Pressure = st.text_input('📈 High Blood Pressure')

with col3:
    Diabetes = st.text_input('🍭 Diabetes')

with col4:
    Heart_Disease = st.text_input('❤️‍🩹 Heart Disease')

with col5:
    Obesity = st.text_input('⚖️ Obesity')

# Code for Prediction
covid19_diagnosis = ''

# Creating a button for Prediction
if st.button('🔍 Covid 19 Test Button'):
    covid19_prediction = covid19.predict([[Fever, Cough, Shortness_of_Breath, Fatigue, Loss_of_Taste_or_Smell,
                                            Sore_Throat, Headache, Muscle_Pain, Diarrhea, Nausea,
                                            Chest_Pain, High_Blood_Pressure, Diabetes, Heart_Disease, Obesity]])

    if covid19_prediction[0] == 1:
        covid19_diagnosis = '🚨 The person is affected by Covid 19'
    else:
        covid19_diagnosis = '✅ The person is not affected by Covid 19'

st.success(covid19_diagnosis)
