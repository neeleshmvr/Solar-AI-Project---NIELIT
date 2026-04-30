from src.data_loader import DataLoader
from src.linear_model import LinearRegression
from src.energy_manager import EnergyManager
import numpy as np

# Load data
loader = DataLoader(
    "data/Plant_1_Generation_Data.csv",
    "data/Plant_1_Weather_Sensor_Data.csv"
)

df = loader.load_data()

# Select useful columns
df = df[["IRRADIATION", "AC_POWER"]]

# Remove empty rows
df = df.dropna()

# Convert to numpy arrays
X = np.array(df["IRRADIATION"])
y = np.array(df["AC_POWER"])

# Create model object
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict for first 5 values
predictions = model.predict(X[:5])

print("Predictions:", predictions)
print("Actual Values:", y[:5])

# Accuracy check

y_pred = model.predict(X)

# R squared score manually
ss_total = np.sum((y - np.mean(y)) ** 2)
ss_residual = np.sum((y - y_pred) ** 2)

r2_score = 1 - (ss_residual / ss_total)

print("Model Accuracy (R2):", round(r2_score, 4))

manager = EnergyManager()

sample_power = predictions[0]

decision = manager.get_decision(sample_power)
revenue = manager.calculate_revenue(sample_power)

print("Decision:", decision)
daily_revenue = revenue * 1000
print("Estimated Daily Revenue (Lakhs):", round(daily_revenue / 100000, 2))