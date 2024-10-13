import streamlit as st

# penggunaan display style magic
import pandas as pd
st.subheader("Stock barang minimarket")
df = pd.DataFrame(
        {
            "nama_barang": ["Susu", "Gula", "Telur", "Minyak Goreng", "Sabun"],
            "harga": [15000, 10000, 20000, 25000, 10000],
            "stok": [10, 15, 20, 25, 15],
        }

)
        
st.dataframe (df)