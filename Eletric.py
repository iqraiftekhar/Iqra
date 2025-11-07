import streamlit as st
import pandas as pd

# Title and description
st.title("⚡ Electricity Bill Analysis App")
st.write("Calculate and analyze your electricity bill using sample data.")

# Load sample data
df = pd.read_csv("sample_data.csv")

# Display sample data
with st.expander("📊 View Sample Data"):
    st.dataframe(df)

# User input section
st.subheader("Enter Your Details")
name = st.text_input("Enter your name:")
units = st.number_input("Enter units consumed (kWh):", min_value=0.0, step=1.0)

# Define tariff rates (example)
rate_chart = {
    "0-100": 3.0,
    "101-300": 4.5,
    "301-500": 6.0,
    "501+": 7.5
}

# Function to calculate bill
def calculate_bill(units):
    if units <= 100:
        return units * rate_chart["0-100"]
    elif units <= 300:
        return (100 * rate_chart["0-100"]) + ((units - 100) * rate_chart["101-300"])
    elif units <= 500:
        return (100 * rate_chart["0-100"]) + (200 * rate_chart["101-300"]) + ((units - 300) * rate_chart["301-500"])
    else:
        return (100 * rate_chart["0-100"]) + (200 * rate_chart["101-300"]) + (200 * rate_chart["301-500"]) + ((units - 500) * rate_chart["501+"])


# Calculate bill when button is clicked
if st.button("🔍 Calculate Bill"):
    if name and units > 0:
        total_bill = calculate_bill(units)

        # Create breakdown DataFrame
        data = {
            "Slab": ["0-100", "101-300", "301-500", "501+"],
            "Rate (₹/unit)": [rate_chart["0-100"], rate_chart["101-300"], rate_chart["301-500"], rate_chart["501+"]],
            "Units Charged": [
                min(units, 100),
                max(min(units - 100, 200), 0),
                max(min(units - 300, 200), 0),
                max(units - 500, 0)
            ]
        }

        bill_df = pd.DataFrame(data)
        bill_df["Cost (₹)"] = bill_df["Rate (₹/unit)"] * bill_df["Units Charged"]

        # Show results
        st.success(f"✅ Electricity Bill for **{name}**")
        st.write("### Bill Breakdown")
        st.dataframe(bill_df)

        st.write(f"### 💰 Total Amount Payable: **₹{total_bill:.2f}**")

        # Analysis message
        if units < 150:
            st.info("Good job! Your consumption is quite low. Keep it up!")
        elif units < 400:
            st.warning("Moderate usage. Consider using power-saving devices.")
        else:
            st.error("High usage detected! Try to reduce your electricity consumption.")
    else:
        st.warning("Please enter your name and units consumed.")
