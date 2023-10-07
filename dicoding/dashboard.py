import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat data yang telah digabungkan
data = pd.read_csv("drive/MyDrive/Dicoding/dataset/bike-sharing-dataset/main_data.csv")

# Mengatur judul halaman
st.title("Dashboard Data Sewa Sepeda")

# Sidebar dengan pilihan
st.sidebar.title("Pilihan")
selected_option = st.sidebar.selectbox("Pilih opsi", ("Distribusi Menurut Musim", "Perbandingan antara Hari Kerja dan Hari Libur"))

# Menampilkan data berdasarkan opsi yang dipilih
if selected_option == "Distribusi Menurut Musim":
    st.header("Distribusi Sewa Sepeda Menurut Musim")

    # Membuat boxplot untuk menampilkan distribusi menurut musim
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=data, order=['Spring', 'Summer', 'Fall', 'Winter'])
    plt.title('Distribusi Jumlah Rental Bike Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Rental Bike')
    st.pyplot(plt)

elif selected_option == "Perbandingan antara Hari Kerja dan Hari Libur":
    st.header("Perbandingan Rata-rata Sewa Sepeda antara Hari Kerja dan Hari Libur")

    # Membuat bar plot untuk menampilkan perbandingan antara hari kerja dan hari libur
    plt.figure(figsize=(8, 5))
    sns.barplot(x='workingday', y='cnt', data=data)
    plt.title('Perbandingan Rata-rata Jumlah Rental Bike antara Hari Kerja dan Hari Libur')
    plt.xlabel('Hari Kerja (0: Hari Libur, 1: Hari Kerja)')
    plt.ylabel('Rata-rata Jumlah Rental Bike')
    st.pyplot(plt)

# Menampilkan tabel data
st.header("Tabel Data")
st.write(data)

# Menyediakan tautan untuk mengunduh data yang telah dibersihkan
st.sidebar.markdown("### Unduh Data yang Telah Dibersihkan")
st.sidebar.write("Anda dapat mengunduh data yang telah dibersihkan dari tautan di bawah ini:")
cleaned_data_url = "main_data.csv"
st.sidebar.markdown(f"[Unduh Data yang Telah Dibersihkan]({cleaned_data_url})")

