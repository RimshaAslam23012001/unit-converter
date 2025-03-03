import streamlit as st
import pandas as pd
import random
import time

# Conversion function for multiple categories (Length, Weight, Temperature)
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        'length': {
            'meters': 1,
            'kilometers': 1000,
            'miles': 1609.34,
            'feet': 0.3048,
            'centimeters': 0.01,
            'inches': 0.0254,
        },
        'weight': {
            'grams': 1,
            'kilograms': 1000,
            'pounds': 453.592,
            'ounces': 28.3495,
        },
        'temperature': {
            'celsius': 1,
            'fahrenheit': 9/5,
            'kelvin': 1,
        }
    }

    if category == 'length':
        value_in_meters = value * conversion_factors['length'][from_unit]
        converted_value = value_in_meters / conversion_factors['length'][to_unit]
    elif category == 'weight':
        value_in_grams = value * conversion_factors['weight'][from_unit]
        converted_value = value_in_grams / conversion_factors['weight'][to_unit]
    elif category == 'temperature':
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            converted_value = (value * 9/5) + 32
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            converted_value = (value - 32) * 5/9
        elif from_unit == 'celsius' and to_unit == 'kelvin':
            converted_value = value + 273.15
        elif from_unit == 'kelvin' and to_unit == 'celsius':
            converted_value = value - 273.15
        elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
            converted_value = (value - 32) * 5/9 + 273.15
        elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
            converted_value = (value - 273.15) * 9/5 + 32
        else:
            converted_value = value
    return converted_value


# Streamlit UI
st.set_page_config(page_title="The Coolest Unit Converter", page_icon="🚀", layout="wide")

# Header with a cool gradient
st.markdown("""
    <style>
        h1 {
            background: linear-gradient(45deg, #FF5F6D, #FFC371);
            -webkit-background-clip: text;
            color: transparent;
            font-size: 4em;
            text-align: center;
        }
        h2 {
            background: linear-gradient(45deg, #6a11cb, #2575fc);
            -webkit-background-clip: text;
            color: transparent;
            font-size: 2.5em;
            text-align: center;
        }
        .stButton > button {
            background-color: #FF5F6D;
            color: white;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
            font-size: 16px;
        }
        .stButton > button:hover {
            background-color: #FFC371;
            transition: all 0.3s ease-in-out;
        }
        .stTextInput input {
            background-color: #FFF8E1;
            border: 2px solid #FF5F6D;
            border-radius: 8px;
            font-size: 18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🚀 **The Coolest Unit Converter** 🚀")
st.header("Transform Your Measurements in Style")

# Sidebar for selecting conversion category
category = st.sidebar.selectbox("Choose Conversion Category", ['Length', 'Weight', 'Temperature'])

# Input fields based on category
if category == 'Length':
    from_unit = st.selectbox("From unit", ['meters', 'kilometers', 'miles', 'feet', 'centimeters', 'inches'])
    to_unit = st.selectbox("To unit", ['meters', 'kilometers', 'miles', 'feet', 'centimeters', 'inches'])
elif category == 'Weight':
    from_unit = st.selectbox("From unit", ['grams', 'kilograms', 'pounds', 'ounces'])
    to_unit = st.selectbox("To unit", ['grams', 'kilograms', 'pounds', 'ounces'])
else:
    from_unit = st.selectbox("From unit", ['celsius', 'fahrenheit', 'kelvin'])
    to_unit = st.selectbox("To unit", ['celsius', 'fahrenheit', 'kelvin'])

# Value input
value = st.number_input("Enter value to convert:", min_value=0.0, step=0.01, label_visibility="visible")

# Storage for conversion history
if 'history' not in st.session_state:
    st.session_state.history = []

# Fun facts for each category
fun_facts = {
    'length': [
        "Did you know? The average length of a marathon is 42.195 kilometers!",
        "Fun Fact: 1 foot is about the size of an average ruler.",
        "A kilometer is roughly the length of 10 football fields!"
    ],
    'weight': [
        "Fun Fact: A standard apple weighs about 200 grams.",
        "Did you know? 1 pound is equivalent to 16 ounces!",
        "A human adult weighs on average between 60-100 kilograms!"
    ],
    'temperature': [
        "Did you know? Water freezes at 0°C and boils at 100°C.",
        "Fun Fact: The hottest temperature recorded on Earth was 56.7°C in Death Valley, USA.",
        "Did you know? Absolute zero is -273.15°C, the coldest possible temperature!"
    ]
}

# Convert when button is clicked
if st.button("✨ Convert Now! ✨"):
    if value > 0:
        # Perform conversion
        converted_value = convert_units(value, from_unit, to_unit, category.lower())
        st.success(f"✨ **{value} {from_unit}** is approximately **{converted_value:.2f} {to_unit}**.")
        
        # Show a fun fact for the conversion
        st.info(random.choice(fun_facts[category.lower()]))
        
        # Add conversion to history
        st.session_state.history.append({"Value": value, "From": from_unit, "To": to_unit, "Converted": converted_value})
        
        # Display an animated spinner while converting (for coolness factor)
        with st.spinner("Converting... 🌀"):
            time.sleep(2)  # Simulate a slight delay for effect
    else:
        st.error("Please enter a positive value.")

# Display the conversion history
if st.session_state.history:
    st.subheader("🔄 Conversion History")
    history_df = pd.DataFrame(st.session_state.history)
    st.dataframe(history_df)

    # Button to clear history
    if st.button("❌ Clear History"):
        st.session_state.history = []  # Clears the history
        st.success("History Cleared! 🔥")

# Fun image or icon for added visual appeal (use any fun, engaging image)
st.image("https://media.giphy.com/media/3o6fJ6PRZp5u5ISMbS/giphy.gif", use_container_width=True, caption="Fun with Units! 🎉")

# Background image (optional) for visual enhancement
st.markdown("""
    <style>
        .reportview-container {
            background-image: url('https://wallpaperaccess.com/full/62627.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
    </style>
""", unsafe_allow_html=True)
