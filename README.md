# 🚗 CO₂ Emission Predictor – Air Pollution Control App

A **Streamlit-based web application** built to estimate CO₂ emissions from vehicles in Pakistan using data from PakWheels.  
The project aims to **raise awareness about air pollution** and encourage **car manufacturers to adopt eco-friendly engine technologies**.

---

## 🌍 Project Goal

To control and monitor air pollution by predicting CO₂ emissions based on car specifications like engine capacity, fuel type, and vehicle age.

This model can:

- ✅ Help policymakers make data-informed decisions  
- ✅ Educate consumers about their vehicle's environmental impact  
- ✅ Signal car manufacturers to innovate sustainable technologies  

---

## 🧠 Model Overview

The model uses:

- **Linear Regression** for CO₂ emission prediction  
- **Fuel-specific emission factors**:

| Fuel Type | Emission Factor (kg/L) |
|-----------|------------------------|
| Petrol    | 2.31                   |
| Diesel    | 2.68                   |
| Hybrid    | 1.60                   |
| CNG       | 2.75                   |
| Electric  | 0.00                   |

---

## 🛠 How to Run This App Locally

# Step 1: Clone the repo
<p>git clone https://github.com/MuhammadUzair17/CO2_Emission_Project.git</p>
<p>cd CO2_Emission_Project</p>

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Launch the Streamlit app
streamlit run co2_app.py

