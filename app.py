#!/usr/bin/env python
# coding: utf-8

#importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle

#filname of final_model
filename = "final_model.pkl"

#function to load the model
def load_model(filename):
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model

loaded_model = load_model(filename)

#function to predict the outcome
def prediction(vector):  
   
    prediction = loaded_model.predict(vector)
    print(prediction)
    return prediction

#take input and predict output
def main():
    
    #front end
    #title of the web
    st.title('Prediction of Insurance Charge')

    st.write('* All Inputs are necessary', color = 'red') #text shown on web

    
    #taking input and converting them to numerical values which our model will understand
    #sex input
    sex = st.radio("What's your sexual orientation?", ("Male", "Female"))
    if sex == "Male":
        s = 1
    else:
        s = 0
    
    #age input
    age = st.slider("How old are you?", 0, 130, 30)
    
    #children input
    children = st.slider("How many children you have?", 0, 20, 0)
    
    #region input
    region = st.selectbox("You belong to which region?", ("southwest", "southeast", "northwest", "northeast"))
    if region == "southwest":
        reg = [0,0,1]
    elif region == "southeast":
        reg = [0,1,0]
    elif region == "northwest":
        reg = [1,0,0]
    else:
        reg = [0,0,0]

    #smoker input
    smoker = st.radio("Do you smoke?", ("Yes", "No"))
    if smoker == "Yes":
        smoke = 1
    else:
        smoke = 0
    
    #bmi input
    bmi = st.slider("What is your BMI?", 0.0, 100.0, 20.0, step = 0.001)

    
    #converting into vector to give input to the model for prediction
    vector = [age, bmi, children, s, smoke]
    vector.extend(reg)
    vector = np.array(vector).reshape(1,-1)
    
   #providing Predict button for prediction
    if st.button("Predict"):
        result = prediction(vector)
        st.success('Your Estimated Insurance Charges are : ${}'.format(round(result[0],2)))


if __name__=='__main__':
    main()



