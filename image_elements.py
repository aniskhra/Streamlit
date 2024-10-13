import streamlit as st

# penggunaan media elements st.image
from PIL import Image
image = Image.open('C:\Streamlit\photo\orange-flower.jpg')

st.image(image, caption='Bunga berwarna oranye yang segar')