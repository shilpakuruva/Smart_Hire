import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# Load saved files

tfidf = pickle.load(
    open("models/tfidf_vectorizer.pkl","rb")
)


job_vectors = pickle.load(
    open("models/job_vectors.pkl","rb")
)


jobs = pd.read_csv(
    "models/jobs_database.csv"
)



def recommend_jobs(resume_text, top_n=5):

    # Convert resume into TF-IDF vector

    resume_vector = tfidf.transform(
        [resume_text]
    )


    # Calculate similarity

    similarity_scores = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]


    # Get top matching jobs

    top_indices = similarity_scores.argsort()[-top_n:][::-1]


    results = jobs.iloc[top_indices].copy()


    results["match_score"] = (
        similarity_scores[top_indices] * 100
    ).round(2)


    return results