#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
import numpy as np
import pandas as pd
import streamlit as st


# In[ ]:


st.title('Electric Motor Temperature: Motor Speed Predictions')
st.write('Random Forest Regressor')


# In[6]:


loaded_model = pickle.load(open('filename', 'rb'))


# In[ ]:


def RandomForest(input_data):
    input_data_asarray = np.asarray(input_data)
    input_data_reshaped = input_data_asarray.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction


# In[ ]:


def user_input_features():
    Ambient = st.sidebar.number_input("Insert ambient")
    Coolant = st.sidebar.number_input("Insert Coolant")
    u_d = st.sidebar.number_input("Insert u_d")
    u_q = st.sidebar.number_input("Insert u_q")
    Torque = st.sidebar.number_input("Insert Torque")
    i_d = st.sidebar.number_input("Insert i_d")
    i_q = st.sidebar.number_input("Insert i_q")
    pm = st.sidebar.number_input("Insert pm")
    stator_yoke = st.sidebar.number_input("Insert stator_yoke")
    stator_tooth = st.sidebar.number_input("Insert stator_tooth")
    stator_winding = st.sidebar.number_input("Insert stator_winding")
    empty = ""

 if st.button("Predict The Motor speed"):
        empty = RandomForest([ambient,coolant,u_d,u_q,i_d,i_q,pm,stator_winding])

st.success(empty)
