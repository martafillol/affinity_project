
## Objective
- Design an advertising tool that matched the content of any publisher website with the interests of the target audience of a given company.
- To achieve this we need to analyze first the content of the website, then the target audience interests and clusters. When we have all of that we can match these based on similarity and show the most suitable ad.

## Data Scraping and Cleaning

1. **Scrape Data from URL:**
   - The `scrape(url)` function collects text data from the given URL. It looks for text inside specific HTML tags like `h1`, `h2`, `p`, etc.

2. **Clean the Scraped Text:**
   - The `text_cleaner(text)` function cleans the collected text by removing numbers, URLs, emails, and punctuation marks. This helps in keeping only the meaningful words.

3. **Combine Scraping and Cleaning:**
   - The `scraper(url)` function uses both the `scrape(url)` and `text_cleaner(text)` functions to get clean text data from the URL.
   - The `scraper_results(url_inputs)` function processes multiple URLs by applying the `scraper(url)` function to each one.

## Embedding and Similarity Calculation

### What is an Embedding?
- An embedding is a way to convert text into numbers so that we can use it with machine learning models. Here, we use the `SentenceTransformer` model to create embeddings for our text.

1. **Load Sentence Transformer Model:**
   - The `SentenceTransformer` model is used to convert the text data into embeddings (numerical representations).

2. **Create Embeddings:**
   - The `embed(text)` function generates an embedding for the given text using the model.

3. **List of Target Interests:**
   - We have a list of interests (like Fashion, Pets, Cooking, etc.) and we create embeddings for each interest.

4. **Calculate Similarity:**
   - We calculate the similarity between the text embedding (from the URL) and the interest embeddings. This helps us find the interest that best matches the text data.

## Cluster Analysis

1. **Load Additional Data:**
   - We load datasets that Wei created, which have user profiles and their retrospective clusters.

2. **Filter Data by Best Fit Interest:**
   - We filter the dataset to find users who have an interest that matches our best fit interest.

3. **Identify the Best Cluster:**
   - We find the cluster with the most occurrences of the best fit interest.

4. **Calculate Average Age:**
   - We calculate the average age of users in the identified cluster.

5. **Find Top 5 Other Interests:**
   - We look at the top 5 other interests that users in the best cluster have.

## Output

- The code outputs the best fit interest, the average age of users in the best cluster, and the top 5 other interests in that cluster.
