import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

covid19 = pickle.load(open('covid19_model.sav', 'rb'))
# page title
st.title('Covid 19 Prediction using ML')


# getting the input data from the user
col1, col2, col3,col4, col5 = st.columns(5)

with col1:
    Fever = st.text_input('Fever  ')
    
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
    Diarrhea= st.text_input('Diarrhea')
    
with col5:
    Nausea = st.text_input('Nausea')

with col1:
  Chest_Pain=st.text_input('Chest_Pain')

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
    covid19_prediction = covid19.predict([[Fever,Cough,Shortness_of_Breath,Fatigue,Loss_of_Taste_or_Smell,Sore_Throat,Headache,Muscle_Pain,Diarrhea,Nausea,Chest_Pain,High_Blood_Pressure,Diabetes,Heart_Disease,Obesity]])
    
    if (covid19_prediction[0] == 1):
      covid19_diagnosis = 'The person is effected by Covid 19'
    else:
      covid19_diagnosis = 'The person is not effected by Covid 19'
    
st.success(covid19_diagnosis)
