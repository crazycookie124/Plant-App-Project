import serial
import csv
from datetime import datetime

# Replace with your ESP32 serial port (check Arduino Tools → Port)
ser = serial.Serial('COM3', 115200)

output_file = "dht11_data_log.csv"

# Create CSV and write header
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'temperature', 'humidity'])

print("📡 Listening to ESP32...")

while True:
    try:
        line = ser.readline().decode().strip()
        if line:
            temp, hum = line.split(',')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(output_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, temp, hum])
                print(f"Logged: {timestamp}, {temp}°C, {hum}%")
    except Exception as e:
        print(f" Error: {e}")
