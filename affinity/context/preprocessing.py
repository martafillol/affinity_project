#get the text from the scraping, clean and embed > output embedding
import spacy

from sentence_transformers import SentenceTransformer
nlp = spacy.load("en_core_web_sm")
# CLEANING
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


# Load sentence transformer model (already pre trained)
model = SentenceTransformer('all-mpnet-base-v2')

# Function to embed text using the model
def embed(text):
    embedding = model.encode(text)
    return embedding
