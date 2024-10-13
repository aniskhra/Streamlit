import streamlit as st
import time

@st.cache # This function will be cached
def my_slow_function(arg1, arg2):
    # Do something really slow in here!
    time.sleep(2)  # Simulate a 2-second delay
    if arg2 == 0:
        return "Tidak bisa membagi dengan nol"
    result = arg1 / arg2
    return f"Hasil: {arg1} ÷ {arg2} = {result}"

# Persist data on disk
@st.cache_data(persist=True)
def fetch_and_clean_data(url):
    # Ambil data dari URL di sini, lalu bersihkan
    return "Data yang sudah diambil dan dibersihkan"

# Demonstrated caching
st.write("Demonstrasi Caching:")
number1 = st.number_input("Masukkan angka pertama:", value=20)
number2 = st.number_input("Masukkan angka kedua:", value=4)

if st.button("Hitung"):
    result = my_slow_function(number1, number2)
    st.write(result)