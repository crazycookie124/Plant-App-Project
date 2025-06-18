import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the combined dataset
df = pd.read_csv("Combined_Sensor_Dataset.csv")

# Label: 1 if moisture < 700 (need water), else 0
df['label'] = df['avgMoisture'].apply(lambda x: 1 if x < 700 else 0)

# Features and target
X = df[['temperature', 'humidity', 'avgMoisture']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
