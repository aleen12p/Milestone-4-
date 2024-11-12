import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV file (make sure the file path is correct)
data_file = '/Users/aleenphimpha/Desktop/Milestone 4/Formatted_Water_Quality_Report.csv'
df = pd.read_csv(data_file)

# Function to create a visual chart based on user selection
def create_chart(substance):
    filtered_data = df[df['Substance'] == substance]

    # Create a bar chart for the selected substance
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data.columns[1:-1], filtered_data.iloc[0, 1:-1], color='skyblue')
    plt.title(f'{substance} Levels in September', fontsize=14)
    plt.xlabel('Locations/Types', fontsize=12)
    plt.ylabel('Concentration (Units)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the chart in Streamlit
    st.pyplot(plt)

# Streamlit UI
st.title('San Jose Water Quality Report - September')
substance_list = df['Substance'].unique()

# Create a dropdown menu for selecting a substance
selected_substance = st.selectbox('Select a Substance:', substance_list)

# Create a button to generate the chart
if st.button('Generate Chart'):
    create_chart(selected_substance)
