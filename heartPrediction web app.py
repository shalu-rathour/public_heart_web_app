# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:37:25 2024

@author: HP
"""
import numpy as np 
import pickle
import streamlit

#loading the saved model
loaded_model = pickle.load(open('C:/Users\HP\Desktop\deploy/heart_disease_model.sav','rb'))

