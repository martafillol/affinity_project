import streamlit as st
import numpy as np
import pandas as pd
import random
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import os
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="Affinity Adv",  # => Quick reference - Streamlit
    page_icon="🪲",
    layout="centered",  # wide
)
CSS = """

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lexend:wght@100..900&family=Varela+Round&display=swap');
h1, h2, h3 {
  font-family: "Lexend", sans-serif;
  font-optical-sizing: auto;
  font-weight: 400;
  font-style: normal;
  color: #ea6106;
  font-size: 2rem;
  text-align: justify;
}
p {
  font-family: "Lexend", sans-serif;
  font-optical-sizing: auto;
  font-weight: 100;
  font-style: normal;
  color: white;
  font-size: 1rem;
}
a {
  text-decoration: none;
  color: white;
  background-color: #ea6106;
  padding: 15px;
  border-radius: 5px;
  transition: 0.3s ease;
}

a:hover {
  background-color: #A36060;
}
"""

st.write(f"<style>{CSS}</style>", unsafe_allow_html=True)


# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'main'


    st.title("Affinity")
    st.write("Predicting the right Ad")

    # Create a form with a submit button
    with st.form(key='my_form'):

        st.write("Fill in the form and press submit to go to the Creative Demo page")
        user_input = st.text_input(label="Enter text here", max_chars=200)
        url = user_input
        response = requests.get("https://affinity-dzgegmrtba-no.a.run.app/process-urls", params={"url_input":url})
        st.write(response.json())
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:

            client = OpenAI()
            best_fit_interest = ['sports','movies','children','party','gaming'][random.randint(0, 4)]
            avg_age_of_cluster = random.randint(18, 80)
            top_5_other_interests = ['fashion', 'gaming', 'movies'][random.randint(0, 2)]
            prompt =    f'''create a realistic advertisement image based on this topic: {best_fit_interest}
                        for a user of age: {int(avg_age_of_cluster)}
                        with top 5 other interests: {top_5_other_interests}.'''
            response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024"
            )
            st.session_state.page = 'creative_demo'
            st.session_state['user_input'] = user_input
            st.session_state['prompt'] = prompt
            st.session_state['response'] = response

    # When the submit button is pressed, set session state to show the creative demo page


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

#
