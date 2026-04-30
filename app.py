import streamlit as st
import numpy as np

from src.linear_model import LinearRegression
from src.energy_manager import EnergyManager
from src.data_loader import DataLoader

st.set_page_config(
    page_title="Solar AI Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
loader = DataLoader(
    "data/Plant_1_Generation_Data.csv",
    "data/Plant_1_Weather_Sensor_Data.csv"
)

df = loader.load_data()
df = df[["IRRADIATION", "AC_POWER"]].dropna()

X = np.array(df["IRRADIATION"])
y = np.array(df["AC_POWER"])

# Train custom model
model = LinearRegression()
model.fit(X, y)

# Create manager
manager = EnergyManager()

# UI
st.markdown("""
<div style='padding:20px;
background: linear-gradient(90deg,#0f172a,#1e293b);
border-radius:15px;'>

<h1 style='text-align:center;color:#facc15;'>
☀️ Solar AI Dashboard
</h1>

<p style='text-align:center;color:white;font-size:18px;'>
AI-Driven Forecasting • Smart Energy Decisions • Revenue Insights
</p>

</div>
""", unsafe_allow_html=True)

st.subheader("Enter Solar Input")

import requests
import pandas as pd

API_KEY = "7015d427dc246d6bc1711c61c0fd0cad"

st.subheader("🌍 Select Location")
city = st.selectbox("Select Indian City", [
    "Hyderabad", "Jaipur", "Bengaluru", "Chennai",
    "Delhi", "Mumbai", "Kolkata", "Ahmedabad",
    "Lucknow", "Bhopal", "Patna", "Amaravati",
    "Thiruvananthapuram", "Ranchi", "Bhubaneswar"
])

# Backup values
city_irradiation = {
    "Hyderabad": 1.0,
    "Jaipur": 1.3,
    "Bengaluru": 0.8,
    "Chennai": 1.1,
    "Delhi": 0.9,
    "Mumbai": 0.7,
    "Kolkata": 0.6,
    "Ahmedabad": 1.2,
    "Lucknow": 0.8,
    "Bhopal": 1.0,
    "Patna": 0.7,
    "Amaravati": 1.1,
    "Thiruvananthapuram": 0.9,
    "Ranchi": 0.8,
    "Bhubaneswar": 0.9
}

irr = city_irradiation[city]

# live weather
try:
   url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"

   data = requests.get(url).json()

   if "main" in data:

       temp = data["main"]["temp"]
       clouds = data["clouds"]["all"]

       irr = max(0.3, 1.4 - (clouds / 100))

       st.success("Live Weather Connected ✅")

       st.write("Live Temperature:", temp)
       st.write("Cloud Cover:", clouds, "%")
       if clouds < 30:
          st.success("☀️ Weather Status: Sunny")
       elif clouds < 70:
          st.info("⛅ Weather Status: Moderate")
       else:
          st.warning("☁️ Weather Status: Cloudy")

   else:
   
       st.warning("Using Offline City Preset Data")

       st.write("Estimated Irradiation:", round(irr, 2))

except:
    st.warning("Using Offline City Preset Data")

st.subheader("⚙️ Run Prediction")

if st.button("Predict"):

    power = model.predict(np.array([irr]))[0]

    decision = manager.get_decision(power)

    Status = manager.Status_decision(power)

    revenue = manager.calculate_revenue(power)
    daily_revenue = revenue * 1000

    col1, col2, col3 = st.columns(3)

    col1.metric("⚡ Power", round(power, 2))
    col2.metric("💰 Revenue", round(daily_revenue / 100000, 2))
    col3.metric("🔋 Status", Status)

    st.success(decision)
    
    st.subheader("📈 Daily Power Trend")
    graph = pd.DataFrame({
        "Time": ["Morning", "Noon", "Evening", "Night"],
        "Power": [power * 0.4, power, power * 0.6, power * 0.2]
    })

    st.subheader("🥧 Power Distribution")

    pie_data = pd.DataFrame({
        "Units": [power * 0.6, power * 0.3, power * 0.1]
    }, index=["Used", "Sold", "Battery"])

    st.bar_chart(pie_data)

    st.line_chart(graph.set_index("Time"))

st.markdown("---")
st.caption("Built using Python • Streamlit • OOP • Custom Linear Regression • Solar AI Project")