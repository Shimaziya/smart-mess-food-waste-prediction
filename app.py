import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load model and dataset
model = joblib.load("mess_waste_model.pkl")
df = pd.read_csv("mess_data.csv")

# Page settings
st.set_page_config(
    page_title="Smart Mess Food Waste Prediction",
    page_icon="🍽️",
    layout="wide"
)

# Title
st.title("🍽️ Smart Mess Food Waste Prediction System")
st.write(
    "Predict food waste and identify the waste risk level "
    "using Machine Learning."
)

st.divider()

# Input section
st.header("Enter Meal Details")

col1, col2 = st.columns(2)

with col1:
    day = st.selectbox(
        "Select Day",
        [
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
    )

    meal = st.selectbox(
        "Select Meal Type",
        ["Breakfast", "Lunch", "Dinner"]
    )

    menu_options = sorted(df["Menu_Type"].unique())

    menu = st.selectbox(
        "Select Menu Type",
        menu_options
    )

with col2:
    students = st.number_input(
        "Students Present",
        min_value=1,
        max_value=500,
        value=170
    )

    food_prepared = st.number_input(
        "Food Prepared (Kg)",
        min_value=1.0,
        max_value=200.0,
        value=45.0
    )

    previous_waste = st.number_input(
        "Previous Day Waste (Kg)",
        min_value=0.0,
        max_value=50.0,
        value=4.0
    )

# Prediction button
if st.button("🔮 Predict Food Waste"):

    input_data = pd.DataFrame({
        "Day": [day],
        "Meal_Type": [meal],
        "Menu_Type": [menu],
        "Students_Present": [students],
        "Food_Prepared_Kg": [food_prepared],
        "Previous_Day_Waste_Kg": [previous_waste]
    })

    prediction = model.predict(input_data)

    predicted_waste = prediction[0]

    # Risk classification
    if predicted_waste < 3:
        risk = "Low"
        recommendation = "Current preparation quantity is suitable."
    elif predicted_waste < 5:
        risk = "Medium"
        recommendation = (
            "Prepare food carefully according to expected students."
        )
    else:
        risk = "High"
        recommendation = "Reduce food preparation quantity."

    st.divider()

    # Results
    st.header("Prediction Result")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        st.metric(
            "Predicted Food Waste",
            f"{predicted_waste:.2f} Kg"
        )

    with result_col2:
        st.metric(
            "Waste Risk",
            risk
        )

    st.info(f"💡 Recommendation: {recommendation}")

# Dashboard statistics
st.divider()
st.header("📊 Mess Waste Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        len(df)
    )

with col2:
    st.metric(
        "Average Waste",
        f"{df['Food_Waste_Kg'].mean():.2f} Kg"
    )

with col3:
    st.metric(
        "Maximum Waste",
        f"{df['Food_Waste_Kg'].max():.2f} Kg"
    )

# Charts
st.subheader("Average Food Waste by Meal")

meal_waste = df.groupby("Meal_Type")["Food_Waste_Kg"].mean()

fig1, ax1 = plt.subplots()
meal_waste.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Meal Type")
ax1.set_ylabel("Average Food Waste (Kg)")
ax1.set_title("Average Food Waste by Meal Type")
plt.xticks(rotation=0)

st.pyplot(fig1)

st.subheader("Average Food Waste by Menu")

menu_waste = (
    df.groupby("Menu_Type")["Food_Waste_Kg"]
    .mean()
    .sort_values()
)

fig2, ax2 = plt.subplots()
menu_waste.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Menu Type")
ax2.set_ylabel("Average Food Waste (Kg)")
ax2.set_title("Average Food Waste by Menu Type")
plt.xticks(rotation=45)

st.pyplot(fig2)

st.success("Smart Mess Food Waste Prediction System is ready!")