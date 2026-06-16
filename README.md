# Project-MachineLearning-SamsulHuda
# Laporan Proyek Machine Learning - Kelayakan Air Minum (Metodologi CRISP-DM)

## Project Overview

<img width="607" height="396" alt="fotoujikelayakanair" src="https://github.com/user-attachments/assets/6b1044f3-6c1c-4502-9ded-eaf2bf841628" />

Akses terhadap air minum yang bersih, aman, dan layak konsumsi merupakan salah satu kebutuhan dasar manusia yang paling krusial sekaligus menjadi pilar penting dalam target *Sustainable Development Goals* (SDGs) nomor 6 mengenai air bersih dan sanitasi. Di banyak daerah, penentuan kualitas kelayakan air masih bertumpu pada pengujian laboratorium manual yang memakan waktu lama dan biaya operasional tinggi. 

Proyek ini hadir untuk mengatasi masalah tersebut dengan membangun sistem prediksi kelayakan air minum secara instan berbasis data tabular kimia air. Pendekatan proyek disusun secara terstruktur menggunakan metodologi standar industri **CRISP-DM (Cross-Industry Standard Process for Data Mining)** serta mengimplementasikan algoritma tingkat tinggi **Extreme Gradient Boosting (XGBoost)** untuk memperoleh akurasi klasifikasi yang optimal.

💡 **Manfaat Proyek:**
* **Efisiensi Lapangan:** Membantu petugas sanitasi mendeteksi kelayakan air minum di pedesaan tanpa harus menunggu hasil lab berhari-hari.
* **Mitigasi Risiko:** Mencegah penyebaran penyakit akibat konsumsi zat kimia berbahaya melalui sistem deteksi dini.
* **Inovasi Komputasi:** Menggunakan arsitektur *ensemble learning* (XGBoost) yang terbukti andal dalam menangani data tabular kompleks dengan *missing values*.

---

## Business Understanding

### 📝 Problem Statements
* Bagaimana cara mengklasifikasikan kelayakan air konsumsi secara cepat dan akurat berdasarkan parameter fisik dan kandungan kimia air?
* Bagaimana cara menangani masalah nilai kosong (*missing values*) yang masif pada dataset kualitas air tanpa merusak performa latih model *machine learning*?

### 🎯 Goals
* Membangun model klasifikasi biner yang mampu membedakan air layak minum (`1`) dan tidak layak minum (`0`) dengan akurasi yang dapat dipertanggungjawabkan.
* Mengurangi angka *False Negative* (kondisi di mana air berbahaya salah terprediksi sebagai air aman) karena berdampak fatal bagi kesehatan publik.

### 🛠️ Solution Approach
* **Extreme Gradient Boosting (XGBoost) Classifier:** Kami memilih algoritma ini karena bekerja dengan mengeksekusi sekumpulan *decision trees* secara bertahap dan mengoreksi kesalahan dari pohon sebelumnya (*boosting*). Algoritma ini memiliki regularisasi bawaan untuk mencegah *overfitting* dan sangat optimal untuk data tabular, memenuhi kriteria **Poin Plus** eksplorasi mandiri di luar materi dasar kelas.

---

## Data Understanding

Dataset yang digunakan bersumber dari Kaggle publik bernama **Water Potability Dataset**. Dataset ini memiliki total ukuran **3.276 baris** dan **10 kolom**.

### 📂 Fitur dan Komponen Dataset:
1. **ph:** Mengukur tingkat keasaman atau kebasaan air (skala ideal menurut WHO: 6.5 - 8.5).
2. **Hardness:** Nilai kekerasan air, dipengaruhi kadar kalsium dan magnesium (mg/L).
3. **Solids:** Total padatan terlarut dalam air (ppm).
4. **Chloramines:** Jumlah senyawa kloramin yang berfungsi sebagai desinfektan (ppm).
5. **Sulfate:** Kadar zat sulfat yang larut di air (mg/L).
6. **Conductivity:** Daya hantar listrik air yang mencerminkan kadar mineral (μS/cm).
7. **Organic_carbon:** Total karbon organik dalam air (ppm).
8. **Trihalomethanes:** Senyawa kimia produk sampingan klorinasi (μg/L).
9. **Turbidity:** Tingkat kekeruhan air berdasarkan properti pemantulan cahaya (NTU).
10. **Potability (Target):** Status kelayakan konsumsi air (`1` = Layak, `0` = Tidak Layak).

### 🔍 Kondisi Awal Data (Eksplorasi):
Setelah dilakukan analisis awal di dalam notebook, ditemukan masalah berupa nilai kosong (*missing values*) pada beberapa fitur krusial:
<img width="467" height="275" alt="image" src="https://github.com/user-attachments/assets/211ca9d7-81be-4be7-874a-e4248e09413e" />
* Kolom `ph`: 491 nilai kosong.
* Kolom `Sulfate`: 781 nilai kosong.
* Kolom `Trihalomethanes`: 162 nilai kosong.
* Rasio target seimbang secara wajar dengan dominasi minor pada kelas air tidak layak.

---

## Data Preparation

Tahapan penyiapan data dilakukan secara teliti untuk memastikan model *machine learning* menerima input data yang berkualitas tinggi:

* **Handling Missing Values (Imputasi Median):** Alih-alih menghapus baris data kosong yang bisa mengurangi informasi, nilai *Null* pada fitur `ph`, `Sulfate`, dan `Trihalomethanes` diisi menggunakan nilai **Median (Nilai Tengah)** dari masing-masing fitur. Pendekatan median dipilih karena lebih aman terhadap pencilan (*outliers*) dibandingkan nilai rata-rata (*mean*).
* **Pemisahan Data (Train-Test Split):**
  Dataset dipisah secara acak menggunakan fungsi `train_test_split` dengan rasio **80% untuk Data Latih (Training Set)** dan **20% untuk Data Uji (Testing Set)**. Proses pemisahan disuntikkan parameter `stratify=y` guna menjamin sebaran rasio label target pada data latih dan data uji sama persis agar model tidak bias.

---

## Modeling

Proyek ini mengimplementasikan algoritma **XGBoost Classifier** dengan konfigurasi parameter sebagai berikut:
* `n_estimators=100` (menggunakan 100 pohon keputusan bertahap).
* `learning_rate=0.1` (mengontrol tingkat penyesuaian bobot model di setiap tahap).
* `max_depth=5` (membatasi kedalaman pohon untuk menghindari kompleksitas berlebih).

**Kelebihan Model:** Mampu memetakan pola hubungan non-linear antar zat kimia air yang rumit dan memiliki komputasi yang sangat cepat.
**Kelemahan Model:** Memerlukan pengawasan *hyperparameter* ketat agar tidak sensitif terhadap noise data hasil imputasi median.

---

## Evaluation

Model diuji secara objektif menggunakan matriks data tes (20% data yang belum pernah dilihat model). Hasil performa evaluasi membuahkan hasil sebagai berikut:

* **Akurasi Model:** Mengalami peningkatan kestabilan di kisaran ~64% hingga 67% menggunakan arsitektur XGBoost.
* **Analisis Karakteristik Data:** Angka akurasi ini merefleksikan kondisi nyata dataset *Water Potability* di mana parameter kimia air memiliki tingkat tumpang tindih (*overlapping*) yang sangat tinggi. Karakteristik ini membuat garis batas keputusan (*decision boundary*) menjadi sangat kompleks.

<img width="510" height="393" alt="image" src="https://github.com/user-attachments/assets/06ee3f5d-1c26-4622-8275-1d10c42a51e6" />

---

## Deployment & Kesimpulan

* **Kesimpulan:** Seluruh rangkaian metodologi CRISP-DM sukses diterapkan, mulai dari penentuan problem bisnis kualitas air, pembersihan data hilang menggunakan metode imputasi median, hingga penerapan pemodelan tingkat tinggi berbasis XGBoost Classifier.
* **Deployment Status:** Model kecerdasan buatan telah diekspor ke dalam berkas `model_xgboost.pkl` dan sukses di-deploy ke peladen awan **Streamlit Community Cloud** secara *live* sehingga pengguna dapat memprediksi kelayakan air secara interaktif melalui peramban web kapan saja.

🔗 **Tautan Aplikasi Live:** [https://project-machinelearning-samsulhuda-dys78sbeuuegt9koggebdp.streamlit.app/]
