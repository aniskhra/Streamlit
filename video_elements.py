import streamlit as st

# penggunaan media elements st.video
video_file = open('C:\Streamlit\clip\orange-flower.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)