#load urls to feed to the model (sitemap + urls) > returns clean list of inventory urls to scrape and saves as csv

from affinity.params import *
from affinity.context.preprocessing import *
import pandas as pd
import requests
import xmltodict
from tqdm import tqdm
import concurrent.futures
from tqdm import tqdm


def visualize_sitemap():
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


#multiprocess to get sitemap urls for the entire sitemap list
def process_sitemap(sitemap_url):
    return fetch_sitemap_urls(sitemap_url)

#all_urls = []

#with concurrent.futures.ThreadPoolExecutor() as executor:
    # Use tqdm to show progress bar
#    results = list(tqdm(executor.map(process_sitemap, sitemap_urls), total=len(sitemap_urls)))

#for result in results:
 #   all_urls.extend(result)


#save list of urls as csv
#inventory_urls= pd.DataFrame()
#inventory_urls["urls"]=all_urls
#inventory_urls.to_csv("/Users/martafillolbruguera/code/affinity_at_scale/data/inventory_urls.csv",index=False)
