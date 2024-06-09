import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Load sentence transformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Load additional datasets
interests_df = pd.read_csv("/Users/martafillolbruguera/code/martafillol/final_project/data/data_v2.csv")
social_media_data = pd.read_csv("/Users/martafillolbruguera/code/martafillol/final_project/data/clean_dataset.csv")
clusters = pd.read_csv("/Users/martafillolbruguera/code/martafillol/final_project/data/data_v2.csv")

# Function to scrape text data from a given URL
def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    scraped_data = []
    html_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
    for tag in html_tags:
        elements = soup.find_all(tag)
        texts = [element.text.strip() for element in elements if len(element.text.strip()) > 30]
        scraped_data.extend(texts)
    scraped_data = pd.Series(scraped_data)
    return scraped_data

# Function to clean the scraped text data
def text_cleaner(text):
    serie_joined = ' '.join(text)
    doc = nlp(serie_joined)
    clean_words = []
    for each in doc:
        if each.is_digit or each.like_url or each.like_email or each.is_punct:
            continue
        else:
            clean_words.append(each)
    return clean_words

# Wrapper function to scrape and clean text data from a given URL
def scraper(url):
    scr = scrape(url)
    clt = text_cleaner(scr)
    words = [each.text for each in clt]
    return ' '.join(words)

# Function to embed text using the model
def embed(text):
    embedding = model.encode(text)
    return embedding

# List of target interests
targets = [
    "Fashion", "Pets", "Cooking", "Fitness", "Movies", "Gaming", "Travel",
    "Cars and automobiles", "Outdoor activities", "Books", "Finance and investments",
    "Business and entrepreneurship", "Photography", "Art", "Social causes and activism",
    "Health and wellness", "Gardening", "Technology", "Education and learning",
    "Sports", "Nature", "History", "Parenting and family", "Music",
    "Food and dining", "DIY and crafts", "Beauty", "Science", "Politics"
]

# Create DataFrame of interests and their embeddings
interests = pd.DataFrame({"interest": targets})
interests["embedding"] = interests.interest.apply(embed)

# Streamlit app
st.title('URL Interest Analyzer')

url = st.text_input('Enter a URL to analyze:', 'https://www.vogue.com/fashion')

if st.button('Analyze'):
    with st.spinner('Analyzing...'):
        try:
            # Scrape and embed text data from the given URL
            text_embedding = embed(scraper(url))

            # Calculate cosine similarity between the text embedding and interest embeddings
            similarities = interests['embedding'].apply(lambda x: cosine_similarity([x], [text_embedding])[0][0])

            # Find the best fit interest
            best_fit_index = similarities.idxmax()
            best_fit_interest = interests.loc[best_fit_index, 'interest']

            # Filter data by best fit interest
            filter_by_interest = clusters.loc[clusters.Interests.str.contains(best_fit_interest, case=False, na=False)]

            if not filter_by_interest.empty:
                # Find the cluster with the most occurrences of the best fit interest
                best_cluster = filter_by_interest.cluster.value_counts().index[0]

                # Calculate the average age of the best cluster
                avg_age_of_cluster = clusters.loc[clusters.cluster == best_cluster].Age.mean()

                # Get data of the best cluster
                best_cluster_df = clusters.loc[clusters.cluster == best_cluster]

                # Evaluate the interests in the best cluster
                best_cluster_df['Interests_eval'] = best_cluster_df.Interests.apply(lambda x: list(eval(x) if ',' in x else [x]))

                # Find the top 5 other interests in the best cluster
                top_5_other_interests = best_cluster_df.explode('Interests_eval').Interests_eval.value_counts()[1:6].index.tolist()

                st.success('Analysis complete!')
                st.write('**Best Fit Interest:**', best_fit_interest)
                st.write('**Average Age of Cluster:**', int(avg_age_of_cluster))
                st.write('**Top 5 Other Interests:**', ', '.join(top_5_other_interests))
            else:
                st.error('No data found for the best fit interest.')

        except Exception as e:
            st.error(f'An error occurred: {e}')
