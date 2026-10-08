import pandas as pd
import random
from datetime import datetime, timedelta

data = []

start_date = datetime(2026, 1, 1)

for i in range(365):

    date = start_date + timedelta(days=i)
    day = date.strftime("%A")

    for meal in ["Breakfast", "Lunch", "Dinner"]:

        # Students present
        if meal == "Breakfast":
            students = random.randint(130, 180)
        elif meal == "Lunch":
            students = random.randint(150, 200)
        else:
            students = random.randint(140, 195)

        # Menu
        if meal == "Breakfast":
            menu = random.choice(["Poha", "Paratha", "Idli", "Bread"])
        elif meal == "Lunch":
            menu = random.choice(["Rice-Dal", "Rajma-Rice", "Chole-Rice", "Veg-Thali"])
        else:
            menu = random.choice(["Roti-Sabzi", "Paneer-Rice", "Dal-Roti", "Special-Thali"])

        # Previous day waste
        previous_waste = random.uniform(2, 7)

        # Base waste depends on meal and menu
        if meal == "Breakfast":
            base_waste = 2.5
        elif meal == "Lunch":
            base_waste = 3.5
        else:
            base_waste = 4.0

        if menu in ["Paratha", "Idli", "Paneer-Rice", "Special-Thali"]:
            base_waste += 0.8

        # Students and previous waste affect today's waste
        waste = (
            base_waste
            + (students - 160) * 0.025
            + previous_waste * 0.20
            + random.uniform(-0.8, 0.8)
        )

        waste = max(1.0, waste)

        # Food prepared is based on students
        prepared = students * random.uniform(0.24, 0.29)

        # Consumed = prepared - waste
        consumed = max(0, prepared - waste)

        data.append([
            date.strftime("%Y-%m-%d"),
            day,
            meal,
            menu,
            students,
            round(prepared, 2),
            round(consumed, 2),
            round(waste, 2),
            round(previous_waste, 2)
        ])


columns = [
    "Date",
    "Day",
    "Meal_Type",
    "Menu_Type",
    "Students_Present",
    "Food_Prepared_Kg",
    "Food_Consumed_Kg",
    "Food_Waste_Kg",
    "Previous_Day_Waste_Kg"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("mess_data.csv", index=False)

print("Realistic dataset generated successfully!")
print("Total rows:", len(df))
print(df.head())