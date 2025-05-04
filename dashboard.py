import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io  # Added this import to fix the error
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Bike Rental Analysis Dashboard",
    page_icon="🚴",
    layout="wide"
)

# Adding a title with better formatting
st.title("🚴 Bike Rental Analysis Dashboard")
st.markdown("""
    *Created by: Frenky Riski Gilang Pratama*  
    *Dicoding ID: m179b4ky1559*  
    *Bangkit Mail: m179b4ky1559@bangkit.academy*
""")

# Add divider
st.divider()

# Load data with caching
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))
    return day_df, hour_df, bike_df

day_df, hour_df, bike_df = load_data()

# Create tabs for better organization
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🌦️ Weather Impact", "📅 Day Type Analysis", "🔍 Data Details"])

with tab1:
    st.header("Dataset Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Daily Data Preview")
        st.dataframe(day_df.head(), use_container_width=True)
        
    with col2:
        st.subheader("Hourly Data Preview")
        st.dataframe(hour_df.head(), use_container_width=True)
    
    st.subheader("Key Statistics")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric("Total Daily Records", len(day_df))
        
    with col4:
        st.metric("Total Hourly Records", len(hour_df))
        
    with col5:
        st.metric("Merged Dataset Records", len(bike_df))
    
    st.subheader("Rental Trends Over Time")
    
    # Convert dteday to datetime
    bike_df['dteday'] = pd.to_datetime(bike_df['dteday'])
    
    fig, ax = plt.subplots(figsize=(12, 6))
    bike_df.groupby('dteday')['cnt_day'].sum().plot(ax=ax)
    plt.title("Total Bike Rentals Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Rentals")
    plt.grid(True)
    st.pyplot(fig)

with tab2:
    st.header("🌦️ Weather Impact Analysis")
    
    st.markdown("""
    ### How does weather affect bike rental patterns?
    This section explores the relationship between weather conditions and bike rental frequency.
    """)
    
    # Weather impact visualization
    weather_hourly = bike_df.groupby("weathersit_hour")["cnt_hour"].mean().reset_index()
    
    # Map weather codes to descriptions
    weather_map = {
        1: "Clear/Few clouds",
        2: "Mist/Cloudy",
        3: "Light Snow/Rain",
        4: "Heavy Rain/Snow"
    }
    weather_hourly['weather_description'] = weather_hourly['weathersit_hour'].map(weather_map)
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(x="weather_description", y="cnt_hour", data=weather_hourly, palette="Blues_d")
    plt.title("Average Hourly Bike Rentals by Weather Condition")
    plt.xlabel("Weather Condition")
    plt.ylabel("Average Hourly Rentals")
    plt.xticks(rotation=45)
    st.pyplot(fig1)
    
    # Additional weather analysis
    st.subheader("Temperature vs. Rentals")
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp_day', y='cnt_day', data=bike_df, alpha=0.5)
    plt.title("Temperature vs. Daily Bike Rentals")
    plt.xlabel("Normalized Temperature")
    plt.ylabel("Total Daily Rentals")
    st.pyplot(fig2)

with tab3:
    st.header("📅 Day Type Analysis")
    
    st.markdown("""
    ### How do bike rentals differ between working days and holidays?
    This section compares rental patterns on different types of days.
    """)
    
    # Day type visualization
    rentals_by_day_type = bike_df.groupby("workingday_day")["cnt_day"].mean().reset_index()
    rentals_by_day_type['day_type'] = rentals_by_day_type['workingday_day'].map({0: "Holiday/Weekend", 1: "Working Day"})
    
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    sns.barplot(x="day_type", y="cnt_day", data=rentals_by_day_type, palette=["#FF6B6B", "#4ECDC4"])
    plt.title("Average Daily Bike Rentals by Day Type")
    plt.xlabel("Day Type")
    plt.ylabel("Average Daily Rentals")
    st.pyplot(fig3)
    
    # Hourly patterns by day type
    st.subheader("Hourly Rental Patterns")
    
    hourly_patterns = bike_df.groupby(['hr', 'workingday_day'])['cnt_hour'].mean().reset_index()
    hourly_patterns['day_type'] = hourly_patterns['workingday_day'].map({0: "Holiday/Weekend", 1: "Working Day"})
    
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt_hour', hue='day_type', data=hourly_patterns, 
                 palette=["#FF6B6B", "#4ECDC4"], linewidth=2.5)
    plt.title("Average Hourly Bike Rentals by Day Type")
    plt.xlabel("Hour of Day")
    plt.ylabel("Average Hourly Rentals")
    plt.xticks(range(0, 24))
    plt.grid(True)
    st.pyplot(fig4)

with tab4:
    st.header("🔍 Dataset Details")
    
    st.subheader("Data Dictionary")
    
    data_dict = {
        "Column": ["dteday", "season", "yr", "mnth", "hr", "holiday", "weekday", "workingday", 
                  "weathersit", "temp", "atemp", "hum", "windspeed", "casual", "registered", "cnt"],
        "Description": ["Date", "Season (1:spring, 2:summer, 3:fall, 4:winter)", 
                       "Year (0:2011, 1:2012)", "Month (1-12)", "Hour (0-23)", 
                       "Whether day is holiday or not", "Day of week", 
                       "If day is neither weekend nor holiday", 
                       "Weather situation (1-4)", "Normalized temperature", 
                       "Normalized feeling temperature", "Normalized humidity", 
                       "Normalized windspeed", "Count of casual users", 
                       "Count of registered users", "Total count of rental bikes"]
    }
    st.dataframe(pd.DataFrame(data_dict), use_container_width=True)
    
    st.subheader("Data Quality Check")
    
    col6, col7 = st.columns(2)
    
    with col6:
        st.write("**Day DataFrame Info:**")
        buffer = io.StringIO()
        day_df.info(buf=buffer)
        st.text(buffer.getvalue())
        
    with col7:
        st.write("**Hour DataFrame Info:**")
        buffer = io.StringIO()
        hour_df.info(buf=buffer)
        st.text(buffer.getvalue())
    
    st.subheader("Missing Values")
    
    col8, col9 = st.columns(2)
    
    with col8:
        st.write("**Day DataFrame Missing Values:**")
        st.dataframe(day_df.isna().sum().to_frame("Missing Values"), use_container_width=True)
        
    with col9:
        st.write("**Hour DataFrame Missing Values:**")
        st.dataframe(hour_df.isna().sum().to_frame("Missing Values"), use_container_width=True)
    
    st.subheader("Duplicate Records")
    
    col10, col11 = st.columns(2)
    
    with col10:
        st.metric("Day DataFrame Duplicates", day_df.duplicated().sum())
        
    with col11:
        st.metric("Hour DataFrame Duplicates", hour_df.duplicated().sum())

# Add footer
st.divider()
st.markdown("""
    *This dashboard was created as part of the Bangkit Academy.*  
    *Data source: [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)*
""")
