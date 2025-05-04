# 🚴 Bike Rental Analysis Dashboard

![alt text](https://github.com/frenskuy/Proyek-Analisis-Data/blob/main/preview.jpg)


## 📌 Overview
This interactive dashboard provides insights into bike rental patterns through data visualization and exploratory analysis. The project analyzes how weather conditions, day types, and temporal factors affect bike rental demand.

**Live Demo**: [frenky data analysis](https://frenkydataanalysisproject.streamlit.app/)

## 🎯 Business Questions Answered
1. **Weather Impact**: How do different weather conditions affect hourly bike rentals?
2. **Day Type Analysis**: How do rental patterns differ between working days and holidays?
3. **Temporal Trends**: What are the overall rental trends over time?

## 🛠️ Technical Implementation
### Tech Stack
- Python 3.9
- Pandas (Data manipulation)
- Seaborn/Matplotlib (Visualization)
- Streamlit (Interactive dashboard)

### Data Sources
[Bike Sharing Dataset from UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)

## 🚀 Getting Started
### Prerequisites
- Python 3.9+
- Conda/Miniconda (recommended)

### Installation
1. Create and activate conda environment:
   ```bash
   conda create --name bike-dashboard python=3.9
   conda activate bike-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib seaborn streamlit
   ```

3. Download dataset files (`day.csv` and `hour.csv`) and place in project root

### Running the Dashboard
```bash
streamlit run dashboard.py
```

## 📊 Dashboard Features
### Interactive Tabs
1. **Overview**: Dataset preview and key metrics
2. **Weather Impact**: Analysis of rental patterns across weather conditions
3. **Day Type Analysis**: Comparison of working days vs holidays
4. **Data Details**: Dataset documentation and quality checks

## 📂 Project Structure
```
proyek-analisis-data/
├── dashboard.py          # Main Streamlit application
├── day.csv               # Daily rental data
├── hour.csv              # Hourly rental data
├── README.md             # Project documentation
├── url.txt               # the url streamlit
└── requirements.txt      # Dependency list
```

## ✉️ Contact
**Frenky Riski Gilang Pratama**  
- Dicoding ID: m179b4ky1559  
- Bangkit Mail: m179b4ky1559@bangkit.academy
