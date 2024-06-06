import streamlit as st
import numpy as np
import pandas as pd
import streamlit_ext as ste
#import streamlit_scrollable_textbox as stx
import streamlit as st


st.set_page_config(initial_sidebar_state="collapsed")

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
        st.session_state.user_input = user_input

# Check if 'page' exists in session state, if not, initialize it
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Display the appropriate page based on the session state
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'creative_demo':
    from creative_demo import creative_demo_page
    creative_demo_page()

# Add a button to navigate back to the main page from the creative demo page
if st.session_state.page == 'creative_demo':
    if st.button("Go Back to Main Page", key='back_to_main'):
        st.session_state.page = 'main'
