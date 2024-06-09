#import data feed to the model
#sitemap fetch urls
#scraping and cleaning urls > scraper_results(url_inputs)

#COLUMN TRANSFORMER
#> embedding



#LDA
#> kmeans to find n of components
#> vectorizer and fitting model to data
#> get embedded text



from context.scrape_clean import scraper_results, scraper, scrape

# List of base sitemap URLs with placeholders for year, month, and week
base_sitemap_urls = [
    "https://www.houseandgarden.co.uk/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.vanityfair.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.epicurious.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.epicurious.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.cntraveller.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.voguebusiness.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.voguebusiness.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://pitchfork.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.self.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.self.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.worldofinteriors.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.worldofinteriors.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.worldofinteriors.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.architecturaldigest.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.newyorker.com/sitemap.xml?year={year}&month={month}&week={week}",
    "https://www.tatler.com/sitemap.xml?year={year}&month={month}&week={week}"
]

# Generate combinations of URLs by changing year, month, and week
sitemap_urls = []
for year in range(2020, 2025):
    for month in range(1, 13):
        for week in range(1, 5):
            for base_url in base_sitemap_urls:
                sitemap_urls.append(base_url.format(year=year, month=month, week=week))

# Print the generated sitemap URLs
for url in sitemap_urls:
    print(url)


#define function for fetching urls for each sitemap

def fetch_sitemap_urls(sitemap_url):
    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:

            dict_data = xmltodict.parse(response.content)

            urls = [entry['loc'] for entry in dict_data['urlset']['url']]

            return urls
    except:
        return []
    else:
        print(f"Failed to fetch {sitemap_url}: Status code {response.status_code}")
    return []


#returns url_inputs list that we will scrape and clean using the scraper_results(url_inputs) function

scraper_results(urls)

#returns text

# Load sentence transformer model (already pre trained)
model = SentenceTransformer('all-mpnet-base-v2')

# Function to embed text using the model
def embed(text):
    embedding = model.encode(text)
    return embedding

#return text_embedding


