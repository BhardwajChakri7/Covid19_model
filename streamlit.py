import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
covid19 = pickle.load(open('covid19_model.sav', 'rb'))

# page title
st.title('Covid 19 Prediction using ML')

# Apply custom styles
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
            background: rgba(0, 0, 0, 0.6);
            padding: 30px;
            border: 2px solid #ccc;
            border-radius: 15px;
            max-width: 800px;
            margin: auto;
            backdrop-filter: blur(10px);
            box-shadow: 0px 8px 30px rgba(0, 0, 0, 0.7);
        }
        .stButton>button {
            background-color: #FF6347;
            color: white;
            font-size: 18px;
            padding: 12px 30px;
            border-radius: 10px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: white;
            color: #FF6347;
            border: 2px solid #FF6347;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: white;
            text-align: center;
            margin-bottom: 20px;
        }
        input[type="text"], input[type="number"], select {
            background-color: white !important;
            color: black !important;
            border: 1px solid #FF6347;
            border-radius: 5px;
            padding: 12px;
            width: 100%;
            max-width: 250px;
            box-sizing: border-box;
        }
        select {
            height: 45px;
            -webkit-appearance: none;
            -moz-appearance: none;
            appearance: none;
        }
        label {
            margin-bottom: 10px;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# getting the input data from the user
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Fever = st.text_input('Fever')
    
with col2:
    Cough = st.text_input('Cough')

with col3:
    Shortness_of_Breath = st.text_input('Shortness_of_Breath')
    
with col4:
    Fatigue = st.text_input('Fatigue')
    
with col5:
    Loss_of_Taste_or_Smell = st.text_input('Loss_of_Taste_or_Smell')
    
with col1:
    Sore_Throat = st.text_input('Sore_Throat')

with col2:
    Headache = st.text_input('Headache')
    
with col3:
    Muscle_Pain = st.text_input('Muscle_Pain')

with col4:
    Diarrhea = st.text_input('Diarrhea')
    
with col5:
    Nausea = st.text_input('Nausea')

with col1:
    Chest_Pain = st.text_input('Chest_Pain')

with col2:
    High_Blood_Pressure = st.text_input('High_Blood_Pressure')
    
with col3:
    Diabetes = st.text_input('Diabetes')

with col4:
    Heart_Disease = st.text_input('Heart_Disease')
    
with col5:
    Obesity = st.text_input('Obesity')

# code for Prediction
covid19_diagnosis = ''

# creating a button for Prediction
if st.button('Covid 19 Test Button'):
    covid19_prediction = covid19.predict([[Fever, Cough, Shortness_of_Breath, Fatigue, Loss_of_Taste_or_Smell, 
                                           Sore_Throat, Headache, Muscle_Pain, Diarrhea, Nausea, 
                                           Chest_Pain, High_Blood_Pressure, Diabetes, Heart_Disease, Obesity]])
    
    if (covid19_prediction[0] == 1):
        covid19_diagnosis = 'The person is affected by Covid 19'
    else:
        covid19_diagnosis = 'The person is not affected by Covid 19'
    
st.success(covid19_diagnosis)
