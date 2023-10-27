import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Muat dataset
df = pd.read_csv("seattle-weather.csv")

# Ekstrak tahun dari kolom date
df['year'] = pd.to_datetime(df['date']).dt.year

st.set_page_config(page_title="Prediksi Cuaca")

st.image("https://images.pexels.com/photos/1796730/pexels-photo-1796730.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", use_column_width=True)

# Judul aplikasi
st.title("PREDIKSI CUACA KOTA SEATTLE")

st.header("")

# Tampilkan dataset dalam bentuk tabel
st.subheader("Dataset Cuaca Kota Seattle")
st.dataframe(df, use_container_width=True)

st.header("")
st.header("")

# Dropdown untuk memilih tahun
selected_year = st.selectbox("Pilih Tahun:", df['year'].unique())

st.header("")

# Filter data berdasarkan tahun yang dipilih
filtered_data = df[df['year'] == selected_year]

# Hitung frekuensi cuaca (weather) untuk setiap tahun
weather_counts = filtered_data['weather'].value_counts()

# Definisikan warna dan label untuk setiap jenis cuaca
colors = ['#00235B', '#E21818', '#FFDD83', '#98DFD6', '#6F69AC']
labels = weather_counts.index

# Tampilkan diagram batang dengan warna dan legenda
st.subheader(f"Diagram Batang Cuaca untuk Tahun {selected_year}")
fig, ax = plt.subplots()
bars = ax.bar(weather_counts.index, weather_counts.values, color=colors, label=labels)
ax.set_xticks(range(len(weather_counts.index)))
ax.set_xticklabels(weather_counts.index, rotation=45)
ax.set_xlabel('Jenis Cuaca')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)


st.header("")
st.header("")


# Tampilkan diagram pie dengan legenda
st.subheader(f"Diagram Pie Cuaca untuk Tahun {selected_year}")
fig, ax = plt.subplots()
ax.pie(weather_counts, labels=weather_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis('equal')  # Agar lingkaran menjadi lingkaran sempurna
st.pyplot(fig)


st.header("")
st.header("")


# Filter data berdasarkan tahun yang dipilih
filtered_data = df[df['year'] == selected_year]

# Temukan nilai tertinggi temp_max untuk tahun yang dipilih
max_temp = filtered_data['temp_max'].max()

# Tampilkan nilai tertinggi temp_max
st.subheader(f"Temperatur Maksimum Tertinggi untuk Tahun {selected_year}")
st.write(f"{max_temp} °C")

st.subheader("")

# Filter data berdasarkan tahun yang dipilih
filtered_data = df[df['year'] == selected_year]

# Temukan nilai terendah temp_min untuk tahun yang dipilih
min_temp = filtered_data['temp_min'].min()

# Tampilkan nilai terendah temp_min
st.subheader(f"Temperatur Minimum Terendah untuk Tahun {selected_year}")
st.write(f"{min_temp} °C")

st.header("")
st.header("")

# Ubah kolom 'date' menjadi tipe datetime
df['date'] = pd.to_datetime(df['date'])

# Ambil bulan Januari, Mei, dan September
filtered_data = df[df['date'].dt.month.isin([1, 5, 9])]


# Plot data untuk bulan Januari, Mei, dan September
st.subheader("Diagram Garis Data Cuaca")
fig, ax = plt.subplots()
ax.plot(filtered_data['date'], filtered_data['precipitation'], label='Precipitation', color='#00235B')
ax.plot(filtered_data['date'], filtered_data['temp_max'], label='Temp Max', color='#E21818')
ax.plot(filtered_data['date'], filtered_data['temp_min'], label='Temp Min', color='#FFDD83')
ax.plot(filtered_data['date'], filtered_data['wind'], label='Wind', color='#98DFD6')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Intensitas / Jumlah")
ax.legend()
plt.xticks(rotation=90)
st.pyplot(fig)