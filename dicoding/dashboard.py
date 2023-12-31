import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat data yang telah digabungkan
data = pd.read_csv("dicoding/main_data.csv")

# Mengatur judul halaman
st.title("Dashboard Data Sewa Sepeda")

# Sidebar dengan pilihan
st.sidebar.title("Pilihan")
selected_option = st.sidebar.selectbox(
    "Pilih opsi",
    ("Distribusi Menurut Musim", "Perbandingan antara Hari Kerja dan Hari Libur"),
)

# Menampilkan data berdasarkan opsi yang dipilih
if selected_option == "Distribusi Menurut Musim":
    st.header("Distribusi Sewa Sepeda Menurut Musim")

    # Visualisasi distribusi jumlah rental bike berdasarkan musim
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(
        x="season", y="cnt", data=data, order=["Spring", "Summer", "Fall", "Winter"]
    )
    plt.title("Distribusi Jumlah Rental Bike Berdasarkan Musim")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Rental Bike")
    st.pyplot(fig)


elif selected_option == "Perbandingan antara Hari Kerja dan Hari Libur":
    st.header("Perbandingan Rata-rata Sewa Sepeda antara Hari Kerja dan Hari Libur")

    # Visualisasi perbandingan rata-rata jumlah rental bike antara hari kerja dan hari libur
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="workingday", y="cnt", data=data)
    plt.title(
        "Perbandingan Rata-rata Jumlah Rental Bike antara Hari Kerja dan Hari Libur"
    )
    plt.xlabel("Hari Kerja (0: Hari Libur, 1: Hari Kerja)")
    plt.ylabel("Rata-rata Jumlah Rental Bike")
    st.pyplot(fig)

# Menampilkan tabel data
st.header("Tabel Data")
st.write(data)

# Menyediakan tautan untuk mengunduh data yang telah dibersihkan
st.sidebar.markdown("### Unduh Data yang Telah Dibersihkan")
st.sidebar.write(
    "Anda dapat mengunduh data yang telah dibersihkan dari tautan di bawah ini:"
)
cleaned_data_url = "main_data.csv"
st.sidebar.markdown(f"[Unduh Data yang Telah Dibersihkan]({cleaned_data_url})")
