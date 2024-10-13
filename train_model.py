import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Data contoh: luas rumah (m²) dan harga rumah (Rp)
house_area = np.array([50, 100, 150, 200, 250, 300, 350, 400, 450, 500]).reshape(-1, 1)
house_price = np.array([50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 500000000])

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(house_area, house_price, test_size=0.2, random_state=42)

# Membuat dan melatih model regresi linier
model = LinearRegression()
model.fit(X_train, y_train)

# Memprediksi dengan data uji (opsional untuk evaluasi)
y_pred = model.predict(X_test)

# Simpan model yang sudah dilatih
joblib.dump(model, 'models/linear_regression_house_price.pkl')

print("Model berhasil disimpan!")