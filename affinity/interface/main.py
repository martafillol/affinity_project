
#input url, scrape, clean, embed
#import target list from params and embed (later imported from audience.)
#calculate similarity between context embedding and target embedding
#filtering function to find best fit interest inside clusters > return best_cluster, avg_age_of_cluster, top_5_other_interests


from affinity.params import * # from audience.model import target list
from affinity.context.preprocessing import *
from affinity.context.loading import *
from affinity.context.model import *
from sklearn.metrics.pairwise import cosine_similarity
from affinity.context.scraper import scraper, scrape

#process url scrape and clean
def process(url): #url is in params
    scr = scrape(url)
    clt = text_cleaner(scr)
    words = [each.text for each in clt]
    return ' '.join(words)


def get_best_interest(url):
    interests = pd.DataFrame({"interest": targets})
    interests["embedding"] = interests.interest.apply(embed)

    # Scrape and embed text data from the given URL
    text_embedding = embed(scraper(url))

    #Calculate cosine similarity between the text embedding and interest embeddings
    similarities = interests['embedding'].apply(lambda x: cosine_similarity([x], [text_embedding])[0][0])

    # Find the best fit interest
    best_fit_index = similarities.idxmax()
    best_fit_interest = interests.loc[best_fit_index, 'interest']

    return best_fit_interest



def analyze_best_cluster(clusters, best_fit_interest):
    # Filter data by best fit interest
    filter_by_interest = clusters.loc[clusters.Interests.str.contains(best_fit_interest)]

    # Find the cluster with the most occurrences of the best fit interest
    best_cluster = filter_by_interest.cluster.value_counts().index[0]

    # Calculate the average age of the best cluster
    avg_age_of_cluster = clusters.loc[clusters.cluster == best_cluster].Age.mean()

    # Get data of the best cluster
    best_cluster_df = clusters.loc[clusters.cluster == best_cluster]

    # Evaluate the interests in the best cluster
    best_cluster_df['Interests_eval'] = best_cluster_df.Interests.apply(lambda x: list(eval(x) if ',' in x else [x]))

    # Find the top 5 other interests in the best cluster
    top_5_other_interests = best_cluster_df.explode('Interests_eval').Interests_eval.value_counts()[1:5]

    return best_cluster, avg_age_of_cluster, top_5_other_interests

def main(url):
    best_fit_interest= get_best_interest(url)
    best_cluster, avg_age_of_cluster, top_5_other_interests = analyze_best_cluster(clusters,best_fit_interest)
    return best_fit_interest, best_cluster, avg_age_of_cluster, top_5_other_interests


if __name__ == "__main__":
    url ='https://www.vogue.com/fashion'

    print(main(url))
