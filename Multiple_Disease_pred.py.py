# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 00:06:31 2024

@author: Vaishnav
"""

import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu
#import numpy as np 

# loading the saved models 
 
diabetes_model = pickle.load(open("D:/python project/project 2/Multiple Disease/saved models/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("D:/python project/project 2/Multiple Disease/saved models/Heart_Disease_model2.sav", 'rb'))

parkinsons_model = pickle.load(open("D:/python project/project 2/Multiple Disease/saved models/Parkinson_Disease_model.sav", 'rb'))


#sidebar for navigate 

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'], 
                           icons=['activity','heart','person'], 
                           default_index = 0)
    
    
# Diabetes Prediction Page 
if (selected == 'Diabetes Prediction'):
    
    # page title 
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    # columns for input fields 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
        
    col1, col2, col3 = st.columns(3)
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    
    # code for Prediction 
    diab_dignosis = ''
    
    # creating a button for Prediction 
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if (diab_prediction[0] == 0):
            diab_dignosis = 'The Person is Not Diabetic'
            
        else:
            diab_dignosis = 'The Person is Diabetic'
    
    st.success(diab_dignosis)
    
    
# Heart Disease Prediction page 
if (selected == 'Heart Disease Prediction'):
    
    # page title 
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age')
    with col2:
        sex = st.text_input('sex')
    with col3:
        cp = st.text_input('chest pain type (4 values)')
    
    col1, col2, col3 = st.columns(3)
   
    with col1:
        trestbps = st.text_input('resting blood pressure')
    with col2:
        chol = st.text_input('serum cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('fasting blood sugar > 120 mg/dl')
        
    col1, col2 = st.columns(2)
    
    with col1:
        restecg = st.text_input('resting electrocardiographic results (values 0,1,2)')
    with col2:
        thalach = st.text_input('maximum heart rate achieved')
        
    col1, col2 = st.columns(2)
    
    with col1:
        exang = st.text_input('exercise induced angina')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
        
    col1, col2 = st.columns(2)
    
    with col1:
        slope = st.text_input('the slope of the peak exercise ST segment')
    with col2:
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
        
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # Ensure all input values are converted to numeric data types
    # Example conversion to float
    
#    age = float(age)
#   sex = float(sex)
#    cp = float(cp)
#    trestbps = float(trestbps)
#    chol = float(chol)
#    fbs = float(fbs)
#    restecg = float(restecg)
#    thalach = float(thalach)
#    exang = float(exang)
#    oldpeak = float(oldpeak)
#    slope = float(slope)
#    ca = float(ca)
#    thal = float(thal)
    
    # code for Prediction 
    heart_dignosis = ''
    
    # creating a button for Prediction 
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
        if (heart_prediction[0] == 0):
            heart_dignosis = 'The Person dose not have a heart disease'
            
        else:
            heart_dignosis = 'The Person hvae a heart disease'
    
    st.success(heart_dignosis)
    
if (selected == 'Parkinsons Prediction'):
    
    # page title 
    st.title('Parkinsons Prediction using ML')
    
    # getting the input data from the user
    # columns for input fields 
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        MDVPFo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVPFhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVPFlo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVPJitter = st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVPJitterA = st.text_input('MDVP:Jitter(Abs)')
        
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        MDVPRAP = st.text_input('SMDVP:RAP')
    with col2:
        MDVPPPQ = st.text_input('MDVP:PPQ')
    with col3:
        JitterDDP = st.text_input('Jitter:DDP')
    with col4:
        MDVPShimmer = st.text_input('MDVP:Shimmer')
    with col5:
        MDVPShimmerd = st.text_input('MDVP:Shimmer(dB)')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        ShimmerAPQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        ShimmerAPQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        MDVPAPQ = st.text_input('MDVPAPQ')
    with col4:
        ShimmerDDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
        
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
        
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    
    # code for Prediction 
    parkinsons_dignosis = ''
    
    # creating a button for Prediction 
    if st.button('Diabetes Test Result'):
        parkinsons_prediction = parkinsons_model.predict([[MDVPFo, MDVPFhi, MDVPFlo, MDVPJitter, MDVPJitterA, MDVPRAP ,MDVPPPQ ,JitterDDP ,MDVPShimmer 
                                                   ,MDVPShimmerd, ShimmerAPQ3, ShimmerAPQ5, MDVPAPQ, ShimmerDDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
    
        if (parkinsons_prediction[0] == 0):
            parkinsons_dignosis = 'The Person is Dose not have a Parkinsons Disease'
            
        else:
            parkinsons_dignosis = 'The Person is have a Parkinsons Disease'
    
    st.success(parkinsons_dignosis)
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    