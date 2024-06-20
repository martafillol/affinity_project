import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# url ='https://www.vogue.com/fashion'


# # MODELING
# # Load Spacy model
# nlp = spacy.load("en_core_web_sm")


# # LOADING
# # Function to scrape text data from a given URL
# def scrape(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     scraped_data = []
#     html_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
#     for tag in html_tags:
#         elements = soup.find_all(tag)
#         texts = [element.text.strip() for element in elements if len(element.text.strip()) > 30]
#         scraped_data.extend(texts)
#     scraped_data = pd.Series(scraped_data)
#     return scraped_data

# # CLEANING
# # Function to clean the scraped text data
# def text_cleaner(text):
#     serie_joined = ' '.join(text)
#     doc = nlp(serie_joined)
#     clean_words = []
#     for each in doc:
#         if each.is_digit or each.like_url or each.like_email or each.is_punct:
#             continue
#         else:
#             clean_words.append(each)
#     return clean_words


# # # MAIN/LOGIC/INTERFACE
# # # Wrapper function to scrape and clean text data from a given URL
# # def scraper(url):
# #     scr = scrape(url)
# #     clt = text_cleaner(scr)
# #     words = [each.text for each in clt]
# #     return ' '.join(words)

# # LOADING
# # Function to process multiple URLs
# def scraper_results(url_inputs):
#     results = []
#     for url in url_inputs:
#         result = scraper(url)
#         results.append(result)
#     return results



# # MODELING
# # Load sentence transformer model
# model = SentenceTransformer('all-mpnet-base-v2')

# #PREPRO
# # Function to embed text using the model
# def embed(text):
#     embedding = model.encode(text)
#     return embedding

# #PARAMS
# # List of target interests
# targets = [
#     "Fashion", "Pets", "Cooking", "Fitness", "Movies", "Gaming", "Travel",
#     "Cars and automobiles", "Outdoor activities", "Books", "Finance and investments",
#     "Business and entrepreneurship", "Photography", "Art", "Social causes and activism",
#     "Health and wellness", "Gardening", "Technology", "Education and learning",
#     "Sports", "Nature", "History", "Parenting and family", "Music",
#     "Food and dining", "DIY and crafts", "Beauty", "Science", "Politics"
# ]


# # MAIN/LOGIC/INTERFACE
# # Create DataFrame of interests and their embeddings
# interests = pd.DataFrame({"interest": targets})
# interests["embedding"] = interests.interest.apply(embed)

# # MAIN/LOGIC/INTERFACE
# # Scrape and embed text data from the given URL
# text_embedding = embed(scraper(url))

# # MAIN/LOGIC/INTERFACE
# # Calculate cosine similarity between the text embedding and interest embeddings
# similarities = interests['embedding'].apply(lambda x: cosine_similarity([x], [text_embedding])[0][0])

# # Find the best fit interest
# best_fit_index = similarities.idxmax()
# best_fit_interest = interests.loc[best_fit_index, 'interest']

# # Print the best fit interest
# print(f"The best fit interest is: {best_fit_interest}")


# LOADING
# Load additional datasets
# interests_df = pd.read_csv("/Users/martafillolbruguera/code/martafillol/final_project/data/data_v2.csv")
# social_media_data = pd.read_csv("/Users/martafillolbruguera/code/martafillol/final_project/data/clean_dataset.csv")
# clusters = pd.read_csv("/Users/martafillolbruguera/code/martafillol/final_project/data/data_v2.csv")


# def analyze_best_cluster(clusters, best_fit_interest):
#     # Filter data by best fit interest
#     filter_by_interest = clusters.loc[clusters.Interests.str.contains(best_fit_interest)]

#     # Find the cluster with the most occurrences of the best fit interest
#     best_cluster = filter_by_interest.cluster.value_counts().index[0]

#     # Calculate the average age of the best cluster
#     avg_age_of_cluster = clusters.loc[clusters.cluster == best_cluster].Age.mean()

#     # Get data of the best cluster
#     best_cluster_df = clusters.loc[clusters.cluster == best_cluster]

#     # Evaluate the interests in the best cluster
#     best_cluster_df['Interests_eval'] = best_cluster_df.Interests.apply(lambda x: list(eval(x) if ',' in x else [x]))

#     # Find the top 5 other interests in the best cluster
#     top_5_other_interests = best_cluster_df.explode('Interests_eval').Interests_eval.value_counts()[1:5]

#     return best_cluster, avg_age_of_cluster, top_5_other_interests



# # FILTERING
# # Filter data by best fit interest
# filter_by_interest = clusters.loc[clusters.Interests.str.contains(best_fit_interest)]

# # Find the cluster with the most occurrences of the best fit interest
# best_cluster = filter_by_interest.cluster.value_counts().index[0]

# # Calculate the average age of the best cluster
# avg_age_of_cluster = clusters.loc[clusters.cluster == best_cluster].Age.mean()

# # Get data of the best cluster
# best_cluster_df = clusters.loc[clusters.cluster == best_cluster]

# # Evaluate the interests in the best cluster
# best_cluster_df['Interests_eval'] = best_cluster_df.Interests.apply(lambda x: list(eval(x) if ',' in x else [x]))

# # Find the top 5 other interests in the best cluster
# top_5_other_interests = best_cluster_df.explode('Interests_eval').Interests_eval.value_counts()[1:5]

# # Making filtering one function and put into # MAIN/LOGIC/INTERFACE

# # Output the best fit interest, average age, and top 5 other interests
# print(best_fit_interest, int(avg_age_of_cluster), top_5_other_interests)
