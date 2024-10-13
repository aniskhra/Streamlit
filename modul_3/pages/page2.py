import streamlit as st
import time

st.markdown("# Page 2 ")
st.sidebar.markdown("# Page 2 : Error box & Spinner")
    
# Penggunaan Error box untuk menampilkan pesan error
e = RuntimeError("Maaf, terjadi kesalahan")
st.exception(e)
    
# Penggunaan spinner
with st.spinner('Tunggu sebentar...'):
    time.sleep(5)
st.success("Selesai!")