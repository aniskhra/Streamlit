import streamlit as st
import time

st.markdown("# Page 4 ")
st.sidebar.markdown("# Page 4 : Snowflakes")
    
# Penggunaan Snowflakes
st.title("Selamat Datang di Dunia Salju!")
st.write("Nikmati efek salju yang menenangkan ❄️")
    
if st.button('Turunkan Salju!'):
    st.toast('3')
    time.sleep(.5)
    st.toast('2')
    time.sleep(.5)
    st.toast('1', icon='🎉')
    st.snow()