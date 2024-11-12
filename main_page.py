import streamlit as st
import pandas as pd
from openai import OpenAI
import openai
import os


openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()


# Load the CSV file (use the correct file path)
data_file = '/Users/aleenphimpha/Desktop/Milestone 4/Formatted_Water_Quality_Report.csv'
df = pd.read_csv(data_file)

# Set your OpenAI API key (replace 'your_api_key_here' with your actual API key)

# Display the first few rows to confirm the data structure
st.write("Column names:", df.columns)
st.write(df.head())  # Show the first few rows for debugging

# Function to generate a summary using ChatGPT
def generate_summary(substance):
    # Filter data for the selected substance
    selected_substance_data = df[df['Substance'] == substance]

    if selected_substance_data.empty:
        return "No data available for this substance."

    # Prepare the text to send to ChatGPT
    summary_text = f"Here is the water quality data for {substance} in September:\n\n"
    for index, row in selected_substance_data.iterrows():
        summary_text += (
            f"- PWTP Influent: {row['PWTP Influent']}\n"
            f"- PWTP Treated: {row['PWTP Treated']}\n"
            f"- RWTP Influent: {row['RWTP Influent']}\n"
            f"- RWTP Treated: {row['RWTP Treated']}\n"
            f"- STWTP Influent: {row['STWTP Influent']}\n"
            f"- STWTP Treated: {row['STWTP Treated']}\n"
            f"- DLR: {row['DLR']}\n"
            f"- MCL: {row['MCL']}\n"
            f"- 2nd MCL: {row['2nd MCL']}\n"
            f"- NL: {row['NL']}\n"
            f"- Units: {row['Units']}\n"
        )

    # Use OpenAI API to generate a concise summary
    response = client.completions.create(model="gpt-3.5-turbo-instruct",
    prompt=summary_text,
    max_tokens=150)
    return response.choices[0].text.strip()

# Streamlit UI
st.title('San Jose Water Quality Report - September')
substance_list = df['Substance'].unique()

# Create a dropdown menu for selecting a substance
selected_substance = st.selectbox('Select a Substance:', substance_list)

# Create a button to generate the summary
if st.button('Get Water Quality Summary'):
    summary = generate_summary(selected_substance)
    st.text(summary)
