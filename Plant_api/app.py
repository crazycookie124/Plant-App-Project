from flask import Flask, request, jsonify
from PIL import Image
import io
import torch
from torchvision import models, transforms

app = Flask(__name__)

# labels for the plant categories
class_names = ['AirPlant', 'Foliage', 'Pothos', 'Succulent', 'Vine']

# model loading
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load("plant_cnn_model.pth", map_location=device))
model.eval().to(device)

# image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        image_name = data.get("image_name")
        if not image_name:
            return jsonify({"error": "Missing image_name"}), 400
        
        image_path = f"./image/{image_name}"
        with open(image_path, "rb") as f:
            img = Image.open(f).convert("RGB")

        img = transform(img).unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(img)
            _, pred = torch.max(output, 1)
            label = class_names[pred.item()]
        
        return jsonify({"prediction": label})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
