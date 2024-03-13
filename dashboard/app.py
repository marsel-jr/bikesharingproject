import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
def load_data():
    hour_csv_path = "dataset/Bike-sharing-dataset/hour.csv"
    day_csv_path = "dataset/Bike-sharing-dataset/day.csv"
    
    data_hour = pd.read_csv(hour_csv_path)
    data_day = pd.read_csv(day_csv_path)
    
    return data_hour, data_day

data_hour, data_day = load_data()

# Pertanyaan 1: Berapa jumlah total sewa sepeda untuk tahun 2012 selama musim gugur (musim 3)?
filtered_data_1 = data_day[(data_day["yr"] == 1) & (data_day["season"] == 3)]
total_sewa_sepeda_1 = filtered_data_1["cnt"].sum()

# Pertanyaan 2: Berapa banyak sepeda sewaan yang digunakan pada hari libur selama musim panas (musim 2) pada tahun 2011?
filtered_data_2 = data_day[(data_day["yr"] == 0) & (data_day["season"] == 2) & (data_day["holiday"] == 1)]
total_sepeda_sewaan_2 = filtered_data_2["cnt"].sum()

# Pertanyaan 3: Bagaimana cara meningkatkan jumlah rental sepeda yang digunakan oleh pengguna biasa (casual) pada hari kerja (hari kerja = 1)?
filtered_data_3 = data_day[(data_day["workingday"] == 1) & (data_day["casual"] > 0)]

# Create Streamlit app
st.title("Proyek Akhir Dicoding")
st.header("Bike Sharing Dashboard")

with st.sidebar:
    st.sidebar.title("About Me!")
    st.sidebar.subheader("Nama")
    st.sidebar.write("Marsel Christian Junior")

    st.sidebar.subheader("Email")
    st.sidebar.write("marsel.jr88@gmail.com")

    st.sidebar.subheader("ID Dicoding")
    st.sidebar.write("marsel_christian_j")

st.header("Menu Pertanyaan")
selected_question = st.selectbox(
    "Pilih Pertanyaan:",
    ("Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3")
)

# Tampilkan pertanyaan yang dipilih
if selected_question == "Pertanyaan 1":
    st.header("Pertanyaan 1:")
    st.write(f"Jumlah total sewa sepeda untuk tahun 2012 selama musim gugur (musim 3): {total_sewa_sepeda_1}")
    
    # Filter tahun 2012 dan musim gugur (season 3)
    filtered_data = data_day[(data_day["yr"] == 1) & (data_day["season"] == 3)]

    # Hitung jumlah total sewa sepeda (cnt)
    total_sewa_sepeda = filtered_data["cnt"].sum()

    # Create a bar chart (visualisasi)
    fig = px.bar(filtered_data, x=filtered_data["dteday"], y=filtered_data["cnt"], hover_data=["dteday", "cnt"])
    fig.update_xaxes(title="Tanggal")
    fig.update_yaxes(title="Jumlah Sewa Sepeda")
    fig.update_layout(title="Visualisasi Jumlah Total Sewa Sepeda untuk Tahun 2012 selama Musim Gugur (Musim 3)")
    st.plotly_chart(fig)
elif selected_question == "Pertanyaan 2":
    st.header("Pertanyaan 2:")
    st.write(f"Jumlah total sepeda sewaan yang digunakan pada hari libur selama musim panas tahun 2011: {total_sepeda_sewaan_2}")
    # Filter tahun 2011, musim panas (season 2), dan hari libur (holiday = 1)
    filtered_data = data_day[(data_day["yr"] == 0) & (data_day["season"] == 2) & (data_day["holiday"] == 1)]
    # Hitung jumlah total sepeda sewaan
    total_sepeda_sewaan = filtered_data["cnt"].sum()
    fig = px.bar(filtered_data, x=filtered_data["dteday"], y=filtered_data["cnt"], hover_data=["dteday", "cnt"])
    fig.update_xaxes(title="Tanggal")
    fig.update_yaxes(title="Jumlah Sepeda Sewaan")
    fig.update_layout(title="Visualisasi Total Sepeda Sewaan yang Digunakan pada Hari Libur")
    st.plotly_chart(fig)
else:
    st.header("Pertanyaan 3:")
    st.write("Bagaimana cara meningkatkan jumlah rental sepeda yang digunakan oleh pengguna biasa (casual) pada hari kerja:")
    fig = px.bar(filtered_data_3, x="weekday", y="casual", title="Jumlah Sewa Sepeda Casual pada Hari Kerja & Strateginya")
    fig.update_xaxes(title="Hari Kerja")
    fig.update_yaxes(title="Visualisasi Jumlah Sewa Sepeda Casual")
    st.plotly_chart(fig)
    
    st.subheader("Strategi guna meningkatkan jumlah rental sepeda:")
    st.write("- Promosi khusus untuk hari-hari tertentu yang memiliki grafik yang rendah seperti pada grafik (Monday & Wednesday), seperti diskon khusus atau penawaran khusus yang hanya berlaku pada hari kerja.")
    st.write("- Memastikan fasilitas penyewaan sepeda, seperti stasiun atau lokasi penyewaan, mudah diakses dan dalam kondisi baik selama hari kerja.")
    st.write("- Mempertimbangkan untuk menambah jumlah sepeda yang tersedia pada hari kerja untuk mengakomodasi permintaan yang lebih tinggi.")
    st.write("- Tingkatkan upaya pemasaran khusus untuk hari kerja, seperti iklan online yang menargetkan pengguna biasa pada hari kerja.")
    st.write("- Membuat program loyalitas atau diskon yang berkelanjutan untuk pengguna biasa yang sering menyewa sepeda pada hari kerja.")
