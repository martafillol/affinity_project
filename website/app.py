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
    page_title="Affinity Adv",
    page_icon="🪲",
    layout="centered",
)
CSS = """

@import url('https://fonts.googleapis.com/css2?family=Anton&family=Lexend:wght@100..900&family=Varela+Round&display=swap');
body {
        background-color: #f0f0f0; /* Replace with your desired color */
    }
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
# with st.form(image.pngkey='my_form'):

#     st.write("Fill in the form and press submit to go to the Creative Demo page")
#     user_input = st.text_input(label="Enter text here", max_chars=200)
#     url = user_input

#     submit_button = st.form_submit_button(label='Submit')
#     if submit_button:
#         response = requests.get("https://affinity-dzgegmrtba-no.a.run.app/process-urls", params={"url_input":url}).json()
#         best_fit_interest = response[0]
#         avg_age_of_cluster = response[1]
#         top_5_other_interests = re.findall(r'\b[^\W\d_]+\b',response[2])[:-2]
#         clusters = [
#     {
#         "age_range": (21, 30),
#         "interests": ["music", "travel", "movies", "technology", "fitness"],
#         "education": ["high school", "college", "associate degree", "bachelor's degree"],
#         "family_status": {"Married": 0.30, "Single": 0.70, "Kids": 0.20},
#         "income_range": (30000, 80000),
#         "car_inspo": "https://www.seat.es/coches/ibiza/modelo",
#         "cluster_name": "Young butterflies",
#         "description": "The young professionals are very active and aim high. With a cosmopolitan view and urban lifestyle they constantly seek for new experiences. The New Ibiza is most likely their first car which is affordable at their stage of career. Urban lifestyle."
#     },
#     {
#         "age_range": (29, 35),
#         "interests": ["travel", "pets", "books", "news & politics", "gardening", "health & wellness", "economy"],
#         "education": ["college", "master's degree", "professional degree"],
#         "family_status": {"Married": 0.60, "Single": 0.40, "Kids": 0.40},
#         "income_range": (40000, 100000),
#         "car_inspo": "https://www.seat.es/coches/arona/modelo",
#         "cluster_name": "Mature heroes",
#         "description": "Grounded individualist is reputable, and people around tend to ask for advice. While being very disciplined and focused on objectives they seek for a thrilling life and are eager to reach a specific status in society. Focused on achieving goals but also taking care of family/pets. Urban + outdoor lifestyle, value nature."
#     },
#     {
#         "age_range": (35, 49),
#         "interests": ["fitness", "fashion", "adventure", "ski", "luxury"],
#         "education": ["high school", "bachelor's degree", "master's degree", "doctorate"],
#         "family_status": {"Married": 0.50, "Single": 0.50, "Kids": 0.50},
#         "income_range": (50000, 150000),
#         "car_inspo": "https://www.cupraofficial.es/coches/leon",
#         "cluster_name": "Ambitious rebels",
#         "description": "individualist, very disciplined. and focused . eager to reach a specific status in society. Focused on achieving goals but also taking care of family/pets. Urban + outdoor lifestyle, value nature."
#     }
# ]




        # client = OpenAI()
        # prompt = f'''Create a realistic advertisement image based on these topics for a car product:
        # Possible interests: {top_5_other_interests},
        # Average age: {avg_age_of_cluster},
        # Specialize the advertisement in the interest: {best_fit_interest},
        # Cluster name: {clusters['cluster_name']},
        # Cluster description: {clusters['description']},
        # Car inspiration: {clusters['car_inspo']}'''
        # response = client.images.generate(
        # model="dall-e-3",
        # prompt=prompt,
        # size="1024x1024"
        # )
        # if response.data and response.data[0] and response.data[0].url:
        #     st.success('Analysis complete!')
        #     st.write('**Best Fit Interest:**', best_fit_interest)
        #     st.write('**Average Age of Cluster:**', int(avg_age_of_cluster))
        #     st.write('**Top Other Interests:**', ', '.join(top_5_other_interests))
        #     image_url = response.data[0].url
        #     st.image(image_url, caption="Generated Image", use_column_width=True)

        # else:
        #     st.write("No image was generated.")

##################################################################################
#--------------------------------------------------------------------------------#
##################################################################################

# Function to inject a banner image above the first <h1> element in a given URL and take a screenshot with predefined resolution


with st.form(key='my_form'):
    st.write("Fill in the form and press submit to go to the Creative Demo page")
    user_input = st.text_input(label="Enter text here", max_chars=200)
    url = user_input
    button = st.form_submit_button("Insert banner")

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
    best_fit_interest = response[0]
    avg_age_of_cluster = response[1]
    top_5_other_interests = re.findall(r'\b[^\W\d_]+\b',response[2])[:-2]
    injected = inject_banner(url, banner_path, output_file, width, height)
    cluster = response[0]
    st.write(cluster)

    if cluster == 0:
        banner_path = banner_path[0]
    elif cluster == 1:
        banner_path = banner_path[1]
    elif cluster == 2:
        banner_path = banner_path[2]
    elif cluster == 3:
        banner_path = banner_path[2]
    elif cluster == 4:
        banner_path = banner_path[2]
    elif cluster == 5:
        banner_path = banner_path[2]
    else:
        st.error('We dont have scenario for this clusyer')

    st.write(banner_path)

    injected = inject_banner(url, banner_path, output_file, width, height)

    if injected:
        st.image(output_file, caption="MMA Banner Screenshot")
        st.success('Analysis complete!')
        st.write('**Best Fit Interest:**', best_fit_interest)
        st.write('**Average Age of Cluster:**', int(avg_age_of_cluster))
        st.write('**Top Other Interests:**', ', '.join(top_5_other_interests))
    else:
            st.write("No image was generated.")



#########

# def main(url):
#     best_fit_interest= get_best_interest(url)
#     best_cluster, avg_age_of_cluster, top_5_other_interests = analyze_best_cluster(clusters,best_fit_interest)
#     return best_fit_interest, best_cluster, avg_age_of_cluster, top_5_other_interests
