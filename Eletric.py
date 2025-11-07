import streamlit as st
import pandas as pd

# -------------------------------------------------
# Title and description
# -------------------------------------------------
st.title("⚡ Electricity Bill Analysis App")
st.write("Calculate and analyze your electricity bill using sample data.")

# -------------------------------------------------
# Local sample data (stored directly in a DataFrame)
# -------------------------------------------------
data = {
    "CustomerName": ["Alice", "Bob", "Charlie", "Diana"],
    "UnitsConsumed": [120, 350, 500, 220],
    "Month": ["January", "January", "January", "January"]
}
df = pd.DataFrame(data)

# Display sample data
with st.expander("📊 View Sample Data"):
    st.dataframe(df)

# -------------------------------------------------
# User Input Section
# -------------------------------------------------
st.subheader("Enter Your Details")
name = st.text_input("Enter your name:")
units = st.number_input("Enter units consumed (kWh):", min_value=0.0, step=1.0)

# -------------------------------------------------
# Define Tariff Rates
# -------------------------------------------------
rate_chart = {
    "0-100": 3.0,
    "101-300": 4.5,
    "301-500": 6.0,
    "501+": 7.5
}

# -------------------------------------------------
# Function to Calculate Bill
# -------------------------------------------------
def calculate_bill(units):
    if units <= 100:
        return units * rate_chart["0-100"]
    elif units <= 300:
        return (100 * rate_chart["0-100"]) + ((units - 100) * rate_chart["101-300"])
    elif units <= 500:
        return (100 * rate_chart["0-100"]) + (200 * rate_chart["101-300"]) + ((units - 300) * rate_chart["301-500"])
    else:
        return (100 * rate_chart["0-100"]) + (200 * rate_chart["101-300"]) +_*_*
