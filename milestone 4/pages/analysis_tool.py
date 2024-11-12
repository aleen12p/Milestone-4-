import streamlit as st
from openai import OpenAI
import openai
import os


# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Streamlit app layout
st.title('Water Analysis Tool')
st.header('What water did you drink today?')

# User input for brand of water
brand_input = st.text_input('Enter the brand of water you drank:')

# Function to get information using ChatGPT (gpt-3.5-turbo)
def get_additional_info(brand):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are an assistant providing detailed information about water brands."},
            {"role": "user", "content": f"Tell me detailed information about the brand {brand} and what substances it may contain in its water product."}
       ],
        max_tokens=1000,
        temperature=0.5)
    return response.choices[0].message.content.strip()

# Display response
if brand_input:
    st.write("Fetching information...")
    try:
        additional_info = get_additional_info(brand_input)
        st.write(f"**Information on {brand_input}**: {additional_info}")
    except Exception as e:
        st.write("An error occurred.")
        st.write(f"Error details: {e}")

  
