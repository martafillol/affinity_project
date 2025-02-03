from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from affinity.interface.main import main

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic model for request body
class URLInput(BaseModel):
    urls: List[str]

@app.get("/")
def root():
    return {'greeting': 'Hello'}

@app.get("/process-urls/")
async def process_urls(url_input: str):
    best_fit_interest, best_cluster, avg_age_of_cluster, top_5_other_interests = main(url_input)
    return {"best_fit_interest": best_fit_interest,
            "best_cluster": int(best_cluster),
            "avg_age_of_cluster": int(avg_age_of_cluster),
            "top_5_other_interests": str(top_5_other_interests)
            }



# Command to run the server: uvicorn api:app --reload
# uvicorn api.fast:app --reload
