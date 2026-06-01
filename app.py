import streamlit as st
import joblib

import pandas as pd
import keras
  
# provide tab title
st.set_page_config("Deployment Project")

#provide the page title
st.title("Booking Status predication")

#Mention description of the problem statement or if you want to mention your name
st.subheader("This project takes multiple details as input and predicts whether booking status is approved or not")
st.subheader(" By Rohini Thorat")