import streamlit as st
AUTHOR = 'OUAIDA YASSINE'




st.write(f'This app was built by {AUTHOR}')
st.text_input('Your email here')
st.date_input('Entrer votre date de naissance')
msg = st.chat_input('Entrer votre message ici : ')

if msg:
  st.write(f'You say : {msg}')
  
