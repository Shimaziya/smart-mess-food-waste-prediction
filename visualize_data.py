import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("mess_data.csv")

# Average waste by meal
meal_waste = df.groupby("Meal_Type")["Food_Waste_Kg"].mean()

plt.figure(figsize=(8, 5))
meal_waste.plot(kind="bar")
plt.title("Average Food Waste by Meal Type")
plt.xlabel("Meal Type")
plt.ylabel("Average Food Waste (Kg)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Average waste by menu
menu_waste = df.groupby("Menu_Type")["Food_Waste_Kg"].mean().sort_values()

plt.figure(figsize=(9, 5))
menu_waste.plot(kind="bar")
plt.title("Average Food Waste by Menu Type")
plt.xlabel("Menu Type")
plt.ylabel("Average Food Waste (Kg)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Students vs food waste
plt.figure(figsize=(8, 5))
plt.scatter(df["Students_Present"], df["Food_Waste_Kg"])
plt.title("Students Present vs Food Waste")
plt.xlabel("Students Present")
plt.ylabel("Food Waste (Kg)")
plt.tight_layout()
plt.show()

print("Visualization completed successfully!")