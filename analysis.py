import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

print("\nFirst 5 rows:")
print(df.head())

# Basic statistics
print("\nStatistics:")
print(df.describe())

# Plot temperature
plt.figure()
plt.plot(df["temperature"], label="Temperature")
plt.title("Temperature Trend")
plt.xlabel("Readings")
plt.ylabel("Temperature")
plt.legend()
plt.show()

# Plot humidity
plt.figure()
plt.plot(df["humidity"], label="Humidity", color='orange')
plt.title("Humidity Trend")
plt.xlabel("Readings")
plt.ylabel("Humidity")
plt.legend()
plt.show()

# Simple anomaly detection
print("\nAnomalies (Temp > 35):")
print(df[df["temperature"] > 35])