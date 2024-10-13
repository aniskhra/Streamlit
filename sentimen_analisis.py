import streamlit as st
import pandas as pd
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Fungsi untuk melakukan analisis sentimen dengan Naive Bayes
def sentimen_naive_bayes(text_input, model, vectorizer):
    transformed_text = vectorizer.transform([text_input])
    prediction = model.predict(transformed_text)[0]
    
    # Klasifikasi hasil sentimen
    if prediction == 1:
        return "Positif :smiley: "
    elif prediction == 0:
        return "Netral 😐"
    elif prediction == -1:
        return "Negatif :angry: "
    return "Tidak Diketahui"

def main():
    st.title("Sentiment Analysis Bahasa Indonesia")
    st.subheader("Streamlit Projects")

    menu = ["Beranda", "Tentang"]
    selection = st.sidebar.selectbox("Menu", menu)
    
    if selection == "Beranda":
        st.subheader("Beranda")
    
        # Mencoba memuat dataset
        try:
            dataset = pd.read_csv("sentiment_twitter.csv", sep='\t', on_bad_lines='skip')
            st.success("Data berhasil dimuat!")
            st.write("Kolom yang ada dalam data: ", dataset.columns.tolist())
            dataset.columns = dataset.columns.str.strip()  # Menghapus spasi ekstra pada nama kolom
        except Exception as error:
            st.error(f"Gagal memuat data: {error}")
            return

        # Memastikan kolom 'sentimen' dan 'Tweet' tersedia
        if 'sentimen' in dataset.columns and 'Tweet' in dataset.columns:
            tweet_column = 'Tweet'
        else:
            st.error("Kolom 'sentimen' atau 'Tweet' tidak tersedia. Pastikan nama kolom sesuai.")
            return

        # Preprocessing data untuk model Naive Bayes
        vectorizer = CountVectorizer()
        X_train = vectorizer.fit_transform(dataset[tweet_column])
        nb_model = MultinomialNB()

        # Melatih model Naive Bayes
        try:
            nb_model.fit(X_train, dataset['sentimen'])
        except Exception as error:
            st.error(f"Terjadi kesalahan saat pelatihan model: {error}")
            return

        # Form input untuk analisis sentimen
        with st.form("formSentimen"):
            user_input = st.text_area("Masukkan teks yang ingin dianalisis")
            analyze_button = st.form_submit_button("Analisis")
        
        # Menampilkan hasil analisis jika tombol ditekan
        if analyze_button and user_input:
            col = st.columns(1)[0]
            
            with col:
                st.info("Hasil")
                sentiment_result = sentimen_naive_bayes(user_input, nb_model, vectorizer)
                st.write(f"Sentimen: {sentiment_result}")
    
    elif selection == "Tentang":
        st.subheader("Tentang Aplikasi")
        st.write("Aplikasi ini menggunakan algoritma Naive Bayes dan TextBlob untuk menganalisis sentimen teks.")
        
if __name__ == '__main__':
    main()