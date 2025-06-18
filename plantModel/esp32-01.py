import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# API endpoint for ESP32-01 device data
url = "https://esp-plant-dashboard.onrender.com/data?deviceID=ESP32-01"

# Send GET request to fetch data
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Request failed with status code: {response.status_code}")

# Parse JSON response
data = response.json()

# Convert JSON data to DataFrame
df = pd.DataFrame(data)

# Convert timestamp strings to datetime objects (likely with timezone info)
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df = df[df['avgMoisture'] != 0]


# Create timezone-aware cutoff timestamp (UTC)
cutoff = datetime.now(timezone.utc) - timedelta(days=30)

# Filter only the data from the last 30 days
df = df[df['timestamp'] > cutoff]

# Save filtered data to CSV
df.to_csv("esp32_moisture_last_30days.csv", index=False)
print(f"✅ Data fetched successfully. {len(df)} records saved to 'esp32_moisture_last_30days.csv'.")
