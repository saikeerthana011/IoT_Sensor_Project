import pandas as pd
import random
import time
from datetime import datetime

def generate_data():
    data = []
    for _ in range(50):  # generate 50 records
        temp = random.uniform(20, 40)   # temperature
        humidity = random.uniform(30, 80)

        data.append({
            "timestamp": datetime.now(),
            "temperature": temp,
            "humidity": humidity
        })
        time.sleep(0.1)

    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)
    print("Data generated and saved to data.csv")

if __name__ == "__main__":
    generate_data()