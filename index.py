import streamlit as st
AUTHOR = 'OUAIDA YASSINE'
import pandas as pd
import numpy as np


st.sidebar.write('Welcome to this sidebar')
st.sidebar.text_input('Enter your data : ')
st.sidebar.button('Click here')
st.write(f'This app was built by {AUTHOR}')
st.text_input('Your email here')
st.date_input('Entrer votre date de naissance')
msg = st.chat_input('Entrer votre message ici : ')

if msg:
  st.write(f'You say : {msg}')
  
