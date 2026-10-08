import pandas as pd
import joblib

# Load trained model
model = joblib.load("mess_waste_model.pkl")

print("======================================")
print(" SMART MESS FOOD WASTE PREDICTION")
print("======================================")

# User inputs
day = input("Enter Day (Monday-Sunday): ")
meal = input("Enter Meal Type (Breakfast/Lunch/Dinner): ")
menu = input("Enter Menu Type: ")
students = int(input("Enter Students Present: "))
food_prepared = float(input("Enter Food Prepared (Kg): "))
previous_waste = float(input("Enter Previous Day Waste (Kg): "))

# Create input data
input_data = pd.DataFrame({
    "Day": [day],
    "Meal_Type": [meal],
    "Menu_Type": [menu],
    "Students_Present": [students],
    "Food_Prepared_Kg": [food_prepared],
    "Previous_Day_Waste_Kg": [previous_waste]
})

# Predict waste
prediction = model.predict(input_data)

predicted_waste = prediction[0]

# Waste risk
if predicted_waste < 3:
    risk = "Low"
elif predicted_waste < 5:
    risk = "Medium"
else:
    risk = "High"

print("\n======================================")
print(" PREDICTION RESULT")
print("======================================")
print("Predicted Food Waste:", round(predicted_waste, 2), "Kg")
print("Waste Risk:", risk)

if risk == "High":
    print("Recommendation: Reduce food preparation quantity.")
elif risk == "Medium":
    print("Recommendation: Prepare food carefully according to expected students.")
else:
    print("Recommendation: Current preparation quantity is suitable.")

print("======================================")