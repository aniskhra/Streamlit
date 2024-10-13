# Core Packages
import streamlit as st
import joblib, os
import numpy as np

# Load the saved model
def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

def main():
    """Prediksi Harga Rumah Berdasarkan Luas"""

    st.title("Prediksi Harga Rumah")

    html_templ = """
    <div style="background-color:#8c7ae6;padding:10px;">
    <h3 style="color:white">Prediksi Harga Rumah Menggunakan Regresi Linier</h3>
    </div>
    """
    st.markdown(html_templ, unsafe_allow_html=True)

    # Menu options
    activity = ["Prediksi Harga Rumah", "Apa itu Regresi Linier?"]
    choice = st.sidebar.selectbox("Menu", activity)

    # House Price Prediction
    if choice == 'Prediksi Harga Rumah':
        st.subheader("Prediksi Harga Rumah")

        # Input: house area in square meters
        house_area = st.slider("Masukkan luas rumah dalam meter persegi", 50, 500)

        if st.button("Prediksi"):
            # Load model
            regressor = load_prediction_model("models/linear_regression_house_price.pkl")
            house_area_reshaped = np.array(house_area).reshape(-1, 1)

            # Predict house price
            predicted_price = regressor.predict(house_area_reshaped)

            st.success(f"Harga estimasi rumah dengan luas {house_area} m²: Rp {predicted_price[0]:,.2f}")

    elif choice == 'Apa itu Regresi Linier?':
        st.subheader("Penjelasan Singkat Regresi Linier")
        st.write("Regresi linier adalah metode statistik yang digunakan untuk memprediksi nilai variabel terikat (dependent) berdasarkan variabel bebas (independent).")

if __name__ == '__main__':
    main()
