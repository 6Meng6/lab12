import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    return pd.read_csv('car_data.csv')

data = load_data()

# Sidebar
st.sidebar.title('Filters')

# Multiselect for transmission type
transmission_options = ['Manual', 'Automatic']
selected_transmission = st.sidebar.multiselect('Select Transmission Type', transmission_options, default=transmission_options)

# Slider for selling price
price_range = st.sidebar.slider('Select Selling Price Range', min_value=0, max_value=50, value=(0, 20))

# Slider for year
year_range = st.sidebar.slider('Select Year Range', min_value=2000, max_value=2024, value=(2000, 2024))

# Button to apply filters
if st.sidebar.button('Apply Filters'):
    filtered_data = data[
        (data['Transmission'].isin(selected_transmission)) &
        (data['Selling_Price'].between(price_range[0], price_range[1])) &
        (data['Year'].between(year_range[0], year_range[1]))
    ]
    st.write(filtered_data)
else:
    st.write(data)
