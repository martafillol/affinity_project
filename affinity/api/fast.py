from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from base.base_model import *

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic model for request body
class URLInput(BaseModel):
    urls: List[str]


@app.post("/process-urls/")
async def process_urls(url_input: URLInput):
    try:
        # Scrape and embed text data from the given URLs
        texts = scraper_results(url_input.urls)
        text_embedding = embed(' '.join(texts))
        # Calculate cosine similarity between the text embedding and interest embeddings
        similarities = interests['embedding'].apply(lambda x: cosine_similarity([x], [text_embedding])[0][0])
        # Find the best fit interest
        best_fit_index = similarities.idxmax()
        best_fit_interest = interests.loc[best_fit_index, 'interest']
        return {"best_fit_interest": best_fit_interest}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# Command to run the server: uvicorn api:app --reload
# uvicorn api.fast:app --reload
