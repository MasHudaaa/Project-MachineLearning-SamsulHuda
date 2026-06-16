import streamlit as st
import pickle
import numpy as np

# 1. Konfigurasi Halaman (Harus di paling atas)
st.set_page_config(
    page_title="Water Potability Smart Checker", 
    page_icon="🚰",
    layout="wide"  # Membuat tampilan web melebar (tidak sempit di tengah)
)

# 2. Load Model Machine Learning
try:
    model = pickle.load(open('model_xgboost.pkl', 'rb'))
except:
    st.error("File 'model_xgboost.pkl' tidak ditemukan di repositori GitHub!")

# 3. Desain Header / Judul Aplikasi dengan Gaya Keren
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🚰 Water Potability Smart Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #4B5563;'>Sistem Deteksi Kelayakan Air Minum Berbasis Inteligensia Buatan (XGBoost)</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #3B82F6;'>", unsafe_allow_html=True)

# Membuat 3 kolom bayangan untuk menaruh gambar tepat di tengah layar
img_col1, img_col2, img_col3 = st.columns([1, 2, 1])

with img_col2: # Gambar dimasukkan ke kolom tengah (kolom ke-2)
    st.image(
        "https://images.unsplash.com/photo-1518156677180-95a2893f3e9f?q=80&w=1000", 
        width=450  # <-- Ukuran pixel sengaja dikunci ke 450 agar ukurannya pas dan ideal
    )

st.write("Masukkan Parameter Indikator Air:")

# 4. PENATAAN LAYOUT (Dibagi Jadi 3 Kolom Biar Tidak Capek Scroll Ke Bawah)
col1, col2, col3 = st.columns(3)

with col1:
    st.info("🧪 **Faktor Keasaman & Kimia**")
    ph = st.slider("1. Nilai pH Air (0 - 14)", 0.0, 14.0, 7.2, step=0.1)
    chloramines = st.number_input("2. Kadar Kloramin (ppm)", value=7.1)
    sulfate = st.number_input("3. Kadar Sulfat (mg/L)", value=333.7)

with col2:
    st.info("🪨 **Kandungan Zat Padat**")
    hardness = st.number_input("4. Kekerasan Air (mg/L)", value=196.3)
    solids = st.number_input("5. Total Padatan Terlarut (ppm)", value=21984.4)
    organic_carbon = st.number_input("6. Karbon Organik (ppm)", value=14.2)

with col3:
    st.info("⚡ **Fisik & Penjernihan**")
    conductivity = st.number_input("7. Daya Hantar Listrik (μS/cm)", value=426.2)
    trihalomethanes = st.number_input("8. Senyawa Trihalometana (μg/L)", value=66.3)
    turbidity = st.slider("9. Tingkat Kekeruhan (NTU)", 0.0, 10.0, 3.9, step=0.1)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Tombol Prediksi Berukuran Besar
st.markdown("<style>div.stButton > button:first-child { background-color: #3B82F6; color: white; width: 100%; font-size: 20px; font-weight: bold; height: 50px; border-radius: 10px; }</style>", unsafe_allow_html=True)

# 6. Eksekusi Prediksi & Tampilan Hasil yang Eye-Catching
if st.button("JALANKAN UJI KELAYAKAN AIR"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(features)
    
    st.markdown("<h3 style='text-align: center;'>HASIL ANALISIS MODEL AI:</h3>", unsafe_allow_html=True)
    
    if prediction[0] == 1:
        # Tampilan Kartu Hijau Besar Jika Layak
        st.markdown("""
        <div style='background-color: #D1FAE5; border-left: 8px solid #10B981; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #065F46; margin: 0;'>AIR DINYATAKAN LAYAK KONSUMSI!</h2>
            <p style='color: #047857; margin: 5px 0 0 0; font-size: 16px;'>Seluruh parameter memenuhi ambang batas aman kesehatan masyarakat berdasarkan pemodelan sekuensial XGBoost.</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons() # Efek balon terbang biar makin meriah pas dapet hasil layak
    else:
        # Tampilan Kartu Merah Besar Jika Tidak Layak
        st.markdown("""
        <div style='background-color: #FEE2E2; border-left: 8px solid #EF4444; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color: #991B1B; margin: 0;'>AIR TIDAK LAYAK KONSUMSI!</h2>
            <p style='color: #B91C1C; margin: 5px 0 0 0; font-size: 16px;'>Bahaya! Ditemukan indikator zat kimia atau properti fisik air yang melampaui batas toleransi tubuh.</p>
        </div>
        """, unsafe_allow_html=True)
