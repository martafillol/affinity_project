import streamlit as st
import numpy as np
import pandas as pd
import random
from openai import OpenAI
import os

st.set_page_config(
    page_title="Affinity Adv",  # => Quick reference - Streamlit
    page_icon="🪲",
    layout="centered",  # wide
)
CSS = """


body {
  font-family: Overpass;
  background-color: #f9ebc88d;
  color: #644536;
  text-align: center;
  padding: 25px;
}

h1, h2, h3 {
  font-family: Roboto;
  color: #0C0A3E;
}

a {
  text-decoration: none;
  color: white;
  background-color: #BA6E6E;
  padding: 15px;
  border-radius: 5px;
  transition: 0.3s ease;
}

a:hover {
  background-color: #A36060;
}
"""

st.write(f"<style>{CSS}</style>", unsafe_allow_html=True)

client = OpenAI()


def generate_prompt(topic, user_age, gender, city, interest):
    return f'''create an image based on this topic: {topic}
               for this website: {st.session_state.page}
               for a user of age: {user_age}, gender: {gender}
               that lives in the city of: {city}. That is interested in {interest}.'''

# Generate a random user context
topic = ['sports','fashion','gaming','movies'][random.randint(0, 3)]
user_age = random.randint(18, 80)
genders = ['male', 'female'][random.randint(0, 1)]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas']
interest = 'User interest'
gender = random.choice(genders)
city = random.choice(cities)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'

prompt = generate_prompt(topic, user_age, gender, city, interest)

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024"
)


def main_page():
    st.title("Title")
    st.write("This is the main page.")

    # Create a form with a submit button
    with st.form(key='my_form'):

        st.write("Fill in the form and press submit to go to the Creative Demo page")
        user_input = st.text_input(label="Enter text here", max_chars=200)
        submit_button = st.form_submit_button(label='Submit')

    # When the submit button is pressed, set session state to show the creative demo page
    if submit_button:
        st.session_state.page = 'creative_demo'
        st.session_state['user_input'] = user_input
        st.session_state['prompt'] = prompt
        st.session_state['response'] = response
        st.experimental_rerun()

# Display the appropriate page based on the session state
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'creative_demo':
    from creative_demo import creative_demo_page
    creative_demo_page(st.session_state['prompt'], st.session_state['response'])

# Add a button to navigate back to the main page from the creative demo page
if st.session_state.page == 'creative_demo':
    if st.button("Go Back to Main Page", key='back_to_main_app'):
        st.session_state.page = 'main'
        st.experimental_rerun()
