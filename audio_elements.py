import streamlit as st

# penggunaan media elements st.audio
audio_file = open('C:\Streamlit\sound\orange_flower.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')