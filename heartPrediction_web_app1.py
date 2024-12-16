# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:04:10 2024

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:37:25 2024

@author: HP
"""
import numpy as np 
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users\HP\Desktop\deploy/heart_disease_model.sav','rb'))

#creating  a function for prediction

def heart_prediction(input_data):
    

    #change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
      return 'The person does not have a heart disease'
    else:
      return 'The person has heart disease'
  
    
def main():
    
    #giving a title
    st.title('Heart prediction web app')
    
    #getting the input data fom the user
   
  
    age = st.text_input('Number of Ages')
    sex = st.text_input('select sex')
    cp = st.text_input('select cp')
    trestbps = st.text_input('select trestbps')
    chol = st.text_input('select chol')
    fbs = st.text_input('select fbs')
    restecg = st.text_input('select restecg')
    thalach = st.text_input('select thalach')
    exang = st.text_input('select exang')
    oldpeak = st.text_input('select oldpeak')
    slope = st.text_input('select slope')
    ca = st.text_input('select ca')
    thal= st.text_input('select thal')
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart disease test result'):
        diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success( diagnosis)
    
    
    
    
if __name__ == '__main__':
        main()
    