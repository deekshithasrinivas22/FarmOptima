import pandas as pd

# ---------------- LOAD DATA ----------------
crop_data = pd.read_csv("dataset/crop.csv")

# ---------------- CLEAN DATA ----------------
crop_data = crop_data.dropna()

# ---------------- FEATURE SELECTION ----------------
X = crop_data[['State_Name', 'Season', 'Crop_Year', 'Area']]
y = crop_data['Crop']

# ---------------- ENCODING ----------------
from sklearn.preprocessing import LabelEncoder

le_state = LabelEncoder()
le_season = LabelEncoder()
le_crop = LabelEncoder()

X['State_Name'] = le_state.fit_transform(X['State_Name'])
X['Season'] = le_season.fit_transform(X['Season'])
y = le_crop.fit_transform(y)

print("Encoding done!")

# ---------------- TRAIN TEST SPLIT ----------------
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Split done!")

# ---------------- MODEL TRAINING ----------------
from sklearn.ensemble import RandomForestClassifier

# Reduced trees → faster training
model = RandomForestClassifier(n_estimators=10)

print("Training model...")
model.fit(X_train, y_train)

print("Model trained!")

# ---------------- PREDICTION ----------------
y_pred = model.predict(X_test)

# ---------------- ACCURACY ----------------
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# ---------------- IRRIGATION MODEL ----------------

# Create irrigation label (simple logic based on Area)
# If area is small → irrigation needed (1), else not needed (0)
crop_data['Irrigation'] = crop_data['Area'].apply(lambda x: 1 if x < 50 else 0)

# Features for irrigation
X_irrigation = crop_data[['Crop_Year', 'Area']]
y_irrigation = crop_data['Irrigation']

# Split
from sklearn.model_selection import train_test_split

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X_irrigation, y_irrigation, test_size=0.2, random_state=42
)

# Train model
from sklearn.linear_model import LogisticRegression

irrigation_model = LogisticRegression()
irrigation_model.fit(X_train_i, y_train_i)

print("\nIrrigation model trained!")

# Predict
y_pred_i = irrigation_model.predict(X_test_i)

# Accuracy
from sklearn.metrics import accuracy_score

print("Irrigation Accuracy:", accuracy_score(y_test_i, y_pred_i))