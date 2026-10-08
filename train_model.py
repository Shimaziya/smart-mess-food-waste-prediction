import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Dataset load
df = pd.read_csv("mess_data.csv")

# Input features
X = df[
    [
        "Day",
        "Meal_Type",
        "Menu_Type",
        "Students_Present",
        "Food_Prepared_Kg",
        "Previous_Day_Waste_Kg"
    ]
]

# Target
y = df["Food_Waste_Kg"]

# Categorical and numerical columns
categorical_features = [
    "Day",
    "Meal_Type",
    "Menu_Type"
]

numerical_features = [
    "Students_Present",
    "Food_Prepared_Kg",
    "Previous_Day_Waste_Kg"
]

# Convert text data into numbers
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)

# Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Complete pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Prediction
y_pred = pipeline.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Training Completed!")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))
joblib.dump(pipeline, "mess_waste_model.pkl")
print("Model saved successfully!")