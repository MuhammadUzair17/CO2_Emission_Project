import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained pipeline
pipeline = joblib.load('co2_emission_model.pkl')

# Page configuration
st.set_page_config(page_title="CO₂ Emission Estimator", layout="centered")

# Main Title
st.title("🌿 CO₂ Emission Estimator (kg/km)")
st.markdown("""
Welcome to the **CO₂ Emission Estimator App**! 🚗💨  
This tool estimates the **carbon dioxide (CO₂) emissions** of a car in **kilograms per kilometer (kg/km)** based on:

- 🛠 **Engine Capacity**  
- 📅 **Vehicle Age**  
- ⛽ **Fuel Type**

""")

# Sidebar: User Input
st.sidebar.header("Enter Car Specifications")
st.sidebar.caption("All values are used to predict CO₂ emissions in **kg per kilometer** of drive.")

engine_capacity = st.sidebar.number_input(
    "🔧 Engine Capacity (cc)",
    min_value=600,
    max_value=6000,
    step=50,
    help="Higher engine capacity typically increases CO₂ emissions (kg/km)."
)

vehicle_age = st.sidebar.number_input(
    "📆 Vehicle Age (in years)",
    min_value=0,
    max_value=50,
    step=1,
    help="Older cars tend to emit more CO₂ due to engine degradation."
)

fuel_type = st.sidebar.selectbox(
    "⛽ Fuel Type",
    ["Petrol", "Diesel", "Hybrid", "CNG", "Electric"],
    help="Fuel type strongly affects CO₂ output per km."
)

# Emission Factor Mapping
def get_emission_factor(fuel):
    factors = {
        'Petrol': 2.31,
        'Diesel': 2.68,
        'Hybrid': 1.60,
        'CNG': 2.75,
        'Electric': 0.0
    }
    return factors.get(fuel, np.nan)

emission_factor = get_emission_factor(fuel_type)

# Emission Estimation Formula
def estimate_emission(cc, factor, age, degradation_rate=0.02):
    return ((cc / 1000) * factor) * (1 + degradation_rate * age)

# Prediction Button
if st.sidebar.button("🚀 Predict CO₂ Emission (kg/km)"):
    if pd.isna(emission_factor):
        st.error("❌ Invalid fuel type selected.")
    else:
        estimated_emission = estimate_emission(engine_capacity, emission_factor, vehicle_age)

        st.subheader("🔍 Prediction Result")
        st.metric(label="Estimated CO₂ Emission", value=f"{estimated_emission:.2f} kg/km")

        # Feedback Based on Emission Level
        if estimated_emission > 2.5:
            st.warning("⚠️ High CO₂ emission per km! Consider improving engine efficiency or switching to cleaner fuels.")
        elif estimated_emission > 1.5:
            st.info("ℹ️ Moderate CO₂ emission per km. There's room for improvement.")
        else:
            st.success("✅ Low CO₂ emission per km. Environmentally friendly choice!")

# Footer
st.markdown("---")
st.caption("Created to support sustainable car manufacturing and cleaner air")
