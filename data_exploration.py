import pandas as pd
import numpy as np


# LOAD DATA


crop_data = pd.read_csv("dataset/crop.csv")

# Remove missing values
crop_data = crop_data.dropna()

# Remove duplicate rows
crop_data = crop_data.drop_duplicates()

# Keep only top 5 crops
top_crops = crop_data['Crop'].value_counts().head(5).index
crop_data = crop_data[crop_data['Crop'].isin(top_crops)]

print("Cleaning done!")


# FEATURE ENGINEERING


# Create Yield Feature
crop_data['Yield'] = crop_data['Production'] / (crop_data['Area'] + 1)

print("Yield feature created!")

# FEATURE SELECTION


X = crop_data[
    [
        'State_Name',
        'District_Name',
        'Season',
        'Crop_Year',
        'Area',
        'Production',
        'Yield'
    ]
]

y = crop_data['Crop']

print("Features selected!")


# TRAIN TEST SPLIT


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Split done!")

#PROCESSING


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

categorical_features = [
    'State_Name',
    'District_Name',
    'Season'
]

numerical_features = [
    'Crop_Year',
    'Area',
    'Production',
    'Yield'
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            'cat',
            OneHotEncoder(handle_unknown='ignore'),
            categorical_features
        ),
        (
            'num',
            StandardScaler(),
            numerical_features
        )
    ]
)

print("Preprocessing done!")



from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    random_state=42
)

# PIPELINE


from sklearn.pipeline import Pipeline

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', model)
])


# TRAIN MODEL


print("Training model...")

pipeline.fit(X_train, y_train)

print("Model trained!")


# PREDICTIONS


y_pred = pipeline.predict(X_test)


# EVALUATION METRICS


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from sklearn.preprocessing import LabelEncoder

# Classification Metrics
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average='weighted'
)

recall = recall_score(
    y_test,
    y_pred,
    average='weighted'
)

f1 = f1_score(
    y_test,
    y_pred,
    average='weighted'
)

# Training & Testing Accuracy
train_score = pipeline.score(X_train, y_train)
test_score = pipeline.score(X_test, y_test)

# MAE, MSE, RMSE, R²


label_encoder = LabelEncoder()

y_test_encoded = label_encoder.fit_transform(y_test)
y_pred_encoded = label_encoder.transform(y_pred)

mae = mean_absolute_error(
    y_test_encoded,
    y_pred_encoded
)

mse = mean_squared_error(
    y_test_encoded,
    y_pred_encoded
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test_encoded,
    y_pred_encoded
)


# DISPLAY RESULTS

print("\n" + "=" * 60)
print("MODEL EVALUATION RESULTS")
print("=" * 60)

print(f"\nTraining Accuracy : {train_score * 100:.2f}%")
print(f"Testing Accuracy  : {test_score * 100:.2f}%")

print(f"\nAccuracy Score    : {accuracy * 100:.2f}%")
print(f"Precision Score   : {precision * 100:.2f}%")
print(f"Recall Score      : {recall * 100:.2f}%")
print(f"F1 Score          : {f1 * 100:.2f}%")

print(f"\nMAE               : {mae:.4f}")
print(f"MSE               : {mse:.4f}")
print(f"RMSE              : {rmse:.4f}")
print(f"R² Score          : {r2:.4f}")

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)
print(classification_report(y_test, y_pred))

print("\n" + "=" * 60)
print("CONFUSION MATRIX")
print("=" * 60)
print(confusion_matrix(y_test, y_pred))