import streamlit as st
AUTHOR = 'OUAIDA YASSINE'
import pandas as pd
import numpy as np

my_js = """
alert("Hola mundo");
"""

# Wrapt the javascript as html code
my_html = f"<script async src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9450187741597742'
     crossorigin='anonymous'>{my_js}</script>"

# Execute your app
st.title("Javascript example")
html(my_html)


st.sidebar.write('Welcome to this sidebar')
st.sidebar.text_input('Enter your data : ')
st.sidebar.button('Click here')
st.write(f'This app was built by {AUTHOR}')
st.text_input('Your email here')
st.date_input('Entrer votre date de naissance')
msg = st.chat_input('Entrer votre message ici : ')

if msg:
  st.write(f'You say : {msg}')
  
