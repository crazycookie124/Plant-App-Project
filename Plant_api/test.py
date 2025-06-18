import requests

url = "http://127.0.0.1:5000/predict"

# 准备文件
files = {
    'file': open(r'C:\Users\Helen\OneDrive\Desktop\plant_api\testPlant1.jpg', 'rb')
}

response = requests.post(url, files=files)
print("Response:", response.text)
print("Status Code:", response.status_code)
print("Content Type:", response.headers['Content-Type'])