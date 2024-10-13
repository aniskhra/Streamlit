import streamlit as st
import time

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 : Balloons")
    
# Penggunaan balloons
st.header("OH, TODAY IS YOUR BIRTHDAY!")

if st.button('Take your balloons!'):
    msg = st.toast('Happy Birthday!', icon='🎉')
    st.balloons()