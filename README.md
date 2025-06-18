![image](https://github.com/user-attachments/assets/b2e2fd2d-7bf3-496d-afed-6744a5109230)

# 🌿 NeoPlant: A Gamified, AI-Driven Plant Care Network
[![Built with Unreal Engine 5](https://img.shields.io/badge/Built%20with-UE5-blueviolet)]()
[![IoT Enabled](https://img.shields.io/badge/IoT-ESP32%20+DHT11-success)]()
[![Made with 💚](https://img.shields.io/badge/Made%20with-%F0%9F%92%9A%20Love%20%26%20Plants-lightgreen)]()
[![Python ML](https://img.shields.io/badge/Machine%20Learning-PyTorch-yellow)]()
[![Contributors](https://img.shields.io/badge/Team-Yufei%2C%20Evie%2C%20Vullnet-blue)]()
###

**Plant Sync – Platform-Based Centralised/Decentralised Plant Care Ecosystem**

NeoPlant transforms everyday plant care into an interactive, community-powered game. Combining **IoT sensors**, **machine learning**, and **Unreal Engine 5**, our system fosters collaboration through **data sharing**, **rewards**, and **real-time simulation** of your plants—both locally and socially.

---

## 🎯 Objective

To create a **technology-powered, gamified platform** where users monitor, nurture, and gamify plant care using real-time sensor data. Through smart automation, AI prediction, and social features, we promote sustainability in a fun and rewarding way.

---

## 🌟 Key Features

- **📷 Plant Classification**  
  Upload a photo to classify your plant into one of 5 categories (succulent, pothos, vine, air plant, foliage).

- **🎮 Pixel Avatar Spawn**  
  Automatically generate and spawn your plant as a pixel-style avatar inside a virtual UE5 room.

- **📡 IoT Sensor Integration**  
  ESP32 + DHT11 sensors monitor real-time soil moisture, temperature, and humidity.

- **💧 Remote Watering System**  
  Trigger an Arduino-controlled pump via the app to hydrate your plant.

- **💚 Health Bar Visualisation**  
  Health bar updates dynamically based on sensor data to reflect plant well-being.

- **🪙 Gamified System**  
  Earn reward coins for timely watering. Spend them in seasonal shops to unlock **XP boosts**, **rare skins**, and **limited quests**.

- **🏡 Friend Garden Mode**  
  Visit friends' virtual gardens, help water their plants, and rank on a seasonal leaderboard.

- **🔗 Smart Contract Inspired Resource Sharing**  
  (Optional) Distributed logic enables decentralized care actions—like alerting nearby users to share excess water or nutrients.

- **🧠 AI-Powered Predictions**  
  Forecast future plant care needs based on trends and past data patterns.

---

## 🧠 Machine Learning Model

![image](https://github.com/user-attachments/assets/58136ce0-0a90-488d-a0c0-c21deb8c470a)

- **Type**: ResNet18 Convolutional Neural Network (CNN)  
- **Framework**: PyTorch (trained via Google Colab)  
- **Classes**:
  - `succulent`
  - `pothos`
  - `vine`
  - `air_plant`
  - `foliage`
- **Model File**: `plant_cnn_model.pth`  
- **Deployment**: REST API via Flask (`/predict`)

---

## 🛠️ System Architecture

```plaintext
User Uploads Plant Photo
        │
   ▶ Flask API (/predict)
        │
   ▶ CNN Classifies Plant
        │
   ▶ UE5 Blueprint Parses Result
        │
   ▶ Pixel Avatar Spawned in Virtual Room
        │
   ▶ Avatar Connects to Sensor Data via Serial
        │
   ▶ Health Bar & Watering Icon Live Update
        │
   ▶ Arduino Triggers Pump if Needed'
 ```
###

### 📁 File Structure
```plaintext
Plant_api/
├── app.py                  # Flask API endpoint
├── plant_cnn_model.pth     # Trained PyTorch model
├── test.py                 # Classification test script

CommunityPlant/
├── Content/
│   ├── Sprites/            # Pixel-style plant avatars
│   └── Blueprints/         # Watering + Health UI logic

esp32/
├── moisture_logger.ino     # Reads moisture & humidity
├── pump_controller.ino     # Controls watering pump
 ```

## 🚀 Deployment Guide

### ✅ Requirements

**Hardware:**
- ESP32 board
- DHT11 sensor
- Arduino-compatible water pump

**Software:**
- Python 3.x
- Flask
- PyTorch
- Unreal Engine 5 (Blueprints enabled)
- Google Colab (for training the model)

---

### ▶️ Run the Flask API Locally

This API receives plant images, performs classification, and sends the result to UE5.

```bash
# Navigate to the API folder
cd plant_api

# Install required dependencies
pip install flask torch torchvision pillow

# Run the API server
python app.py
```
The server will run at http://localhost:5000/predict by default.

---

## 👥 Contributors

This project was created with love, curiosity, and lots of plant waterings by:

- **🪴 Yufei** – ML Engineer and UI Designer 
- **🌸 Evie** – Game Designer and Software Engineer
- **🌿 Vullnet** – Product Manager and UX Researcher

> Special thanks to our pixel plants for never giving up on us 🌱

