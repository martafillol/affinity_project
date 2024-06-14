import streamlit as st
import random
import requests
from openai import OpenAI
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
import time
import base64
st.set_page_config(
    page_title="Affinity at Scale",
    page_icon="🪲",
    layout="centered",
)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Hammersmith+One&family=Lexend:wght@100..900&family=Varela+Round&display=swap');
body {
    background-color: #f0f0f0; /* Replace with your desired color */
}

h2, h3 {
    text-align: center;
  font-size: 2.5em;
  font-weight: bold;
  color: #f19137;
  margin-bottom: 20px;
  padding: 10px;

}

.st-emotion-cache-1jzia57 .e1nzilvr3 {
    visibility: hidden;
    display: none;
}

.centered-title {
  text-align: center;
  font-size: 3em;
  font-weight: bold;
  color: #f19137;
  margin-bottom: 20px;

  padding: 10px;
  border-radius: 20%;
}

.centered-button {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

p {
    font-family: "Lexend", sans-serif;
    font-optical-sizing: auto;
    font-weight: 200;
    font-style: normal;
    color: black;
    font-size: 1rem;
}

a {
    text-decoration: none;
    display: none;
    color: white;
    padding: 15px;
    border-radius: 5px;
    transition: 0.3s ease;
}

"""
st.write(f"<style>{CSS}</style>", unsafe_allow_html=True)

st.markdown("<h1 class='centered-title'>Affinity at Scale</h1>", unsafe_allow_html=True)




##################################################################################
#--------------------------------------------------------------------------------#
##################################################################################

# Function to inject a banner image above the first <h1> element in a given URL and take a screenshot with predefined resolution


with st.form(key='my_form_1'):
    st.markdown('<div class="centered-form">', unsafe_allow_html=True)
    st.write("Enter Publisher Url")
    user_input = st.text_input(label="", max_chars=200)
    url = user_input
    button = st.form_submit_button("Submit")
    st.markdown('</div>', unsafe_allow_html=True)

def inject_banner(url, banner_path, output_file, width, height):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for testing
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")  # Larger window size

    driver = None
    try:
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=chrome_options,
        )

        # Set the window size to the predefined resolution
        driver.set_window_size(width, height)

        # Open the given URL
        driver.get(url)
        time.sleep(5)  # Increased wait time for the page to load

        # Read the local image file and encode it as a base64 string
        with open(banner_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()

        # Create a base64 data URL
        banner_url = f"data:image/png;base64,{encoded_string}"

        # Inject a banner image above the first <h1> element
        script = f"""
        var banner = document.createElement("img");
        banner.src = "{banner_url}";
        banner.style.width = "100%";
        banner.style.height = "100px";
        var h1 = document.querySelector("h1");
        if (h1) {{
            h1.parentNode.insertBefore(banner, h1);
        }}
        """
        driver.execute_script(script)
        time.sleep(5)  # Wait for the script to execute

        # Take a screenshot with the predefined resolution
        driver.save_screenshot(output_file)
        print(f"Screenshot saved as {output_file}")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        if driver:
            driver.quit()


banner_path = ["website/banners/YOUNG.png","website/banners/MATURE.png","website/banners/AMBITIOUS.png"]
output_file = "injected_banner_screenshot.png"
width = 728
height = 1080

if button:
    response = requests.get("https://affinity-dzgegmrtba-no.a.run.app/process-urls", params={"url_input":url}).json()
    best_fit_interest = response["best_fit_interest"]
    avg_age_of_cluster = response["avg_age_of_cluster"]
    top_5_other_interests = re.findall(r'\b[^\W\d_]+\b',response["top_5_other_interests"])[:-2]
    injected = inject_banner(url, banner_path, output_file, width, height)
    cluster = int(response["best_cluster"])


    if cluster == 0:
        banner_path = banner_path[0]
    elif cluster == 1:
        banner_path = banner_path[0]
    elif cluster == 2:
        banner_path = banner_path[1]
    elif cluster == 3:
        banner_path = banner_path[1]
    elif cluster == 4:
        banner_path = banner_path[2]
    elif cluster == 5:
        banner_path = banner_path[2]
    else:
        banner_path = banner_path[3]


    injected = inject_banner(url, banner_path, output_file, width, height)

    if injected:
        st.success('Analysis complete!')
        #st.write('**Topic:**', best_fit_interest)
        st.title(f'Topic:  {best_fit_interest}')

        st.image(output_file, caption="MMA Banner Screenshot")
        #st.write('**Average Age of Cluster:**', int(avg_age_of_cluster))
        #st.write('**Top Other Interests:**', ', '.join(top_5_other_interests))
    else:
            st.write("No image was generated.")


st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)


##################################################################################
#--------------------------------------------------------------------------------#
##################################################################################


st.markdown("<h2>AI generated Ad</h2>", unsafe_allow_html=True)

with st.form(key='my_form'):
    st.write("")
    user_input = st.text_input(label="Enter Publisher Url", max_chars=200)
    url = user_input
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        response = requests.get("https://affinity-dzgegmrtba-no.a.run.app/process-urls", params={"url_input": url}).json()
        best_fit_interest = response["best_fit_interest"]
        avg_age_of_cluster = response["avg_age_of_cluster"]
        top_5_other_interests = re.findall(r'\b[^\W\d_]+\b', response["top_5_other_interests"])[:-2]
        cluster = int(response["best_cluster"])

        clusters_ai = [
            {
                "age_range": (21, 30),
                "interests": ["music", "travel", "movies", "technology", "fitness"],
                "education": ["high school", "college", "associate degree", "bachelor's degree"],
                "family_status": {"Married": 0.30, "Single": 0.70, "Kids": 0.20},
                "income_range": (30000, 80000),
                "car_inspo": "car inspire in ibiza model",
                "cluster_name": "Young butterflies",
                "description": "The young professionals are very active and aim high. With a cosmopolitan view and urban lifestyle they constantly seek for new experiences."
            },
            {
                "age_range": (29, 35),
                "interests": ["travel", "pets", "books", "news & politics", "gardening", "health & wellness", "economy"],
                "education": ["college", "master's degree", "professional degree"],
                "family_status": {"Married": 0.60, "Single": 0.40, "Kids": 0.40},
                "income_range": (40000, 100000),
                "car_inspo": "car inspire in arona model",
                "cluster_name": "Mature heroes",
                "description": "Grounded individualist is reputable, While being very disciplined and focused on objectives they seek for a thrilling life and are eager to reach a specific status in society. Focused on achieving goals but also taking care of family/pets. value nature."
            },
            {
                "age_range": (35, 49),
                "interests": ["fitness", "fashion", "adventure", "ski", "luxury"],
                "education": ["high school", "bachelor's degree", "master's degree", "doctorate"],
                "family_status": {"Married": 0.50, "Single": 0.50, "Kids": 0.50},
                "income_range": (50000, 150000),
                "car_inspo": "car inspire in leon model",
                "cluster_name": "Ambitious rebels",
                "description": "Individualist, very disciplined and focused, eager to reach a specific status in society. Focused on achieving goals but also taking care of family/pets. Urban."
            }
        ]
        if cluster == 0:
            cluster_ai = 0
        elif cluster == 1:
            cluster_ai = 0
        elif cluster == 2:
            cluster_ai = 1
        elif cluster == 3:
            cluster_ai = 1
        else:
            cluster_ai = 2
        selected_cluster = clusters_ai[cluster_ai]

        client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])
        prompt = f'''Create a photorealistic advertisement image based on these topics for a car product:
        Possible interests: {top_5_other_interests},
        Average age: {avg_age_of_cluster},
        Specialize the advertisement in the interest: {best_fit_interest},
        Cluster name: {selected_cluster['cluster_name']},
        Cluster description: {selected_cluster['description']},
        Car inspiration: {selected_cluster['car_inspo']}'''
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024"
        )
        if response.data and response.data[0] and response.data[0].url:
            st.success('Analysis complete!')
            st.write('**Best Fit Interest:**', best_fit_interest)
            image_url = response.data[0].url
            st.image(image_url, caption="Generated Image", use_column_width=True)
        else:
            st.write("No image was generated.")
