
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

# Function to process multiple URLs
def scraper_results(url_inputs):
    results = []
    for url in url_inputs:
        result = scraper(url)
        results.append(result)
    return results
