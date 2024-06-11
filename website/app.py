import streamlit as st
import random
import requests
from openai import OpenAI
import re


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



st.title("Affinity")
st.write("Predicting the right Ad")

# Create a form with a submit button
with st.form(key='my_form'):

    st.write("Fill in the form and press submit to go to the Creative Demo page")
    user_input = st.text_input(label="Enter text here", max_chars=200)
    url = user_input

    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        response = requests.get("https://affinity-dzgegmrtba-no.a.run.app/process-urls", params={"url_input":url}).json()
        best_fit_interest = response[0]
        avg_age_of_cluster = response[1]
        top_5_other_interests = re.findall(r'\b[^\W\d_]+\b',response[2])[:-2]

        client = OpenAI()

        prompt =    f'''create a realistic advertisement image based on this topic: {best_fit_interest}
                    for a user of age: {int(avg_age_of_cluster)}
                    with other top interests: {top_5_other_interests}.'''
        response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024"
        )
        if response.data and response.data[0] and response.data[0].url:
            st.success('Analysis complete!')
            st.write('**Best Fit Interest:**', best_fit_interest)
            st.write('**Average Age of Cluster:**', int(avg_age_of_cluster))
            st.write('**Top Other Interests:**', ', '.join(top_5_other_interests))
            image_url = response.data[0].url
            st.image(image_url, caption="Generated Image", use_column_width=True)

        else:
            st.write("No image was generated.")
