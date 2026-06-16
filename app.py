import streamlit as st
import pickle
import numpy as np
import pandas as pd

# 1. Load Model Machine Learning yang sudah dibuat di Colab
try:
    model = pickle.load(open('model_xgboost.pkl', 'rb'))
except:
    st.error("File 'model_xgboost.pkl' tidak ditemukan di repositori GitHub!")

st.set_page_config(page_title="Water Potability Checker", page_icon="🚰")

st.title("Aplikasi Klasifikasi Kelayakan Air Minum 🚰")
st.write("Metodologi CRISP-DM dengan Implementasi Algoritma XGBoost")
st.markdown("---")

st.write("Silakan masukkan nilai parameter fisik dan kimia air di bawah ini:")

# 2. Form Input User berbentuk Slider & Number Input
ph = st.slider("1. Nilai pH Air (0 - 14)", 0.0, 14.0, 7.0, step=0.1)
hardness = st.number_input("2. Kekerasan Air (Hardness) dalam mg/L", value=196.3)
solids = st.number_input("3. Total Padatan Terlarut (Solids) dalam ppm", value=21984.4)
chloramines = st.number_input("4. Kadar Kloramin (Chloramines) dalam ppm", value=7.1)
sulfate = st.number_input("5. Kadar Sulfat (Sulfate) dalam mg/L", value=333.7)
conductivity = st.number_input("6. Daya Hantar Listrik (Conductivity) dalam μS/cm", value=426.2)
organic_carbon = st.number_input("7. Total Karbon Organik (Organic Carbon) dalam ppm", value=14.2)
trihalomethanes = st.number_input("8. Senyawa Trihalometana dalam μg/L", value=66.3)
turbidity = st.number_input("9. Tingkat Kekeruhan Air (Turbidity) dalam NTU", value=3.9)

st.markdown("---")

# 3. Proses Prediksi Saat Tombol Diklik
if st.button("Uji Kelayakan Air Now!"):
    # Satukan semua input menjadi array data yang siap diprediksi
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    # Lakukan prediksi (0 atau 1)
    prediction = model.predict(features)
    
    # Tampilkan Hasil ke Layar Web
    if prediction[0] == 1:
        st.success("🎉 HASIL: Air Dinyatakan LAYAK untuk Dikonsumsi!")
    else:
        st.error("🚨 HASIL: Air TIDAK LAYAK! Mengandung Zat Berbahaya.")