import streamlit as st

# Set page configuration at the very beginning
st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")

# Conversion functions for Length, Weight, and Temperature
def convert_length(value, from_unit, to_unit):
    conversions = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    }
    if from_unit == to_unit:
        return value
    return value * (conversions[to_unit] / conversions[from_unit])

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462
    }
    if from_unit == to_unit:
        return value
    return value * (conversions[to_unit] / conversions[from_unit])

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    elif from_unit == to_unit:
        return value
    return value  # Default return value

# CSS for styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
            color: #333;
            font-family: 'Poppins', sans-serif;
        }
        .stButton>button {
            background-color: #ff5e57;
            color: white;
            font-weight: bold;
            border-radius: 30px;
            width: 100%;
            padding: 14px;
            text-align: center;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #ff1c00;
        }
        .stTextInput>div>input, .stSelectbox>div>div>input {
            background-color: #ffffff;
            border: 1px solid #ff5e57;
            border-radius: 30px;
            padding: 14px;
            font-size: 16px;
            color: #333;
        }
        .stAlert {
            background-color: #ffebee;
            color: #d32f2f;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
        }
        .stSuccess {
            background-color: #e8f5e9;
            color: #388e3c;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)

# App title
st.markdown('<h1 style="text-align: center; font-size: 3rem; color: #ff5e57; font-weight: 900;">🔢 Unit Converter</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; color: #333; font-size: 1.5rem; font-weight: 400;">Convert Length, Weight, or Temperature with Ease</h3>', unsafe_allow_html=True)

# Conversion categories
category = st.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

# Category-based unit selection
categories = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Kilograms", "Grams", "Pounds"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From", categories[category])
to_unit = st.selectbox("To", categories[category])
value = st.number_input("Enter value", min_value=0.0, format="%.2f", step=0.01)

# Error handling
if value <= 0 and category != "Temperature":
    st.error("Please enter a positive value greater than zero.")

# Perform conversion
if "results" not in st.session_state:
    st.session_state.results = []

if st.button("Convert"):
    result = None
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)

    if result is not None:
        result_text = f"✅ {value} {from_unit} = **{result:.4f} {to_unit}**"
        st.success(result_text)
        st.session_state.results.append(result_text)

# Show conversion history
if st.session_state.results:
    st.markdown("### 🔄 Conversion History")
    for res in st.session_state.results[-5:]:
        st.write(res)

# Footer
st.markdown('<div style="text-align: center; font-size: 12px; color: #888888;">Made with ❤️ by Kiran</div>', unsafe_allow_html=True)
