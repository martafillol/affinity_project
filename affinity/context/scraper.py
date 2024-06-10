
import requests
from bs4 import BeautifulSoup
import pandas as pd
import spacy
from spacymoji import Emoji
from affinity.context.preprocessing import text_cleaner

url = 'https://medium.com/@getgoing.ca/the-ultimate-guide-to-choosing-the-perfect-car-19747eec95e'

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("emoji", first=True)


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

scrape_data = scrape(url)

def scraper(url):
    scr = scrape(url)
    clt = text_cleaner(scr)
    words = [each.text for each in clt]
    return ' '.join(words)

def scraper_results(url_inputs):
    results =[]
    for url in url_inputs:
        result = scraper(url)
        results.append(result)
    return results
#
