# ☀️ Solar-AI-Project---NIELIT

An AI-based solar power forecasting and energy management project developed using Python and Streamlit. This project predicts solar AC power generation using weather and irradiation data, displays revenue insights, and provides simple smart energy suggestions.

## 📌 Project Overview

Solar power generation changes based on sunlight, weather, and cloud conditions. This project helps in estimating solar power output and supports better energy planning.

The system uses a custom Linear Regression model to predict AC power generation and shows the results through an interactive dashboard.

## 🚀 Features

* Predicts solar AC power output
* Uses custom Linear Regression model
* Indian city selection support
* Live weather API with backup preset values
* Revenue estimation based on generated power
* Smart recommendations for battery usage or selling extra power
* Interactive dashboard using Streamlit
* Graphs and charts for result visualization

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Streamlit
* Requests API
* Visual Studio Code

## 📂 Project Structure

```text
Solar AI Project
│── data
│   ├── Plant_1_Generation_Data.csv
│   ├── Plant_1_Weather_Sensor_Data.csv
│
│── src
│   ├── data_loader.py
│   ├── linear_model.py
│   ├── energy_manager.py
│
│── main.py
│── app.py
```

## ▶️ How to Run the Project

1. Install required libraries:

```bash
pip install pandas numpy streamlit requests
```

2. Run the dashboard:

```bash
streamlit run app.py
```

## 📊 Output

The dashboard displays:

* Predicted AC Power
* Revenue Estimation
* Weather Status
* Daily Power Trend Graph
* Power Distribution Chart

## 🔮 Future Improvements

* Multi-plant support
* Advanced machine learning models
* Real-time IoT sensor integration
* Battery optimization system
* Smart grid connectivity

## 👨‍💻 Author
Developed as an academic project









Developed as an academic project for solar power forecasting and energy management.

