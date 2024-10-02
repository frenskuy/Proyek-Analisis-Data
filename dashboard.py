import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Adding a title
st.title("Bike Rental Analysis")
st.write("Frenky Riski Gilang Pratama")
st.write("Dicoding ID : m179b4ky1559")
st.write("Bangkit Mail : m179b4ky1559@bangkit.academy")

# Load data
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Merge dataframes
bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))

# Data wrangling and exploration
# Assessing data
day_info = day_df.info()
hour_info = hour_df.info()

day_missing_values = day_df.isna().sum()
hour_missing_values = hour_df.isna().sum()

day_duplicates = day_df.duplicated().sum()
hour_duplicates = hour_df.duplicated().sum()

# Cleaning data
# No cleaning needed as per the provided code.

# Exploratory Data Analysis (EDA)
# Visualizations
# Pertanyaan 1
weather_hourly = bike_df.groupby("weathersit_hour")["cnt_hour"].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x="weathersit_hour", y="cnt_hour", data=weather_hourly)
plt.title("Pengaruh Cuaca terhadap Jumlah Penyewaan sepeda per Jam")
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Jumlah Penyewaan Sepeda per Jam")
plt.xticks(ticks=[0, 1, 2, 3], labels=['Springer', 'Summer', 'Fall', 'Winter'])
st.pyplot(plt)

# Pertanyaan 2
rentals_by_day_type = bike_df.groupby("workingday_day")["cnt_day"].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x="workingday_day", y="cnt_day", data=rentals_by_day_type)
plt.title("Perbedaan Jumlah Penyewaan Sepeda antara Hari Kerja dan Hari Libur")
plt.xlabel("Hari Kerja(1) / Hari Libur(0)")
plt.ylabel("Rata-rata Jumlah Penyewaan Sepeda")
plt.xticks(ticks=[0,1], labels=["Hari Libur", "Hari Kerja"])
st.pyplot(plt)

# Displaying Dataframe and other information if needed
st.subheader("Data Info")
st.write("Day DataFrame Info:", day_info)
st.write("Hour DataFrame Info:", hour_info)

st.subheader("Missing Values")
st.write("Day DataFrame Missing Values:", day_missing_values)
st.write("Hour DataFrame Missing Values:", hour_missing_values)

st.subheader("Duplicates")
st.write("Day DataFrame Duplicates:", day_duplicates)
st.write("Hour DataFrame Duplicates:", hour_duplicates)
