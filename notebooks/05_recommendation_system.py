import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load processed datasets
resume_df = pd.read_csv("data/processed/resume_processed.csv")
linkedin_df = pd.read_csv("data/processed/linkedin_processed.csv")
naukri_df = pd.read_csv("data/processed/naukri_processed.csv")

print("Datasets loaded successfully!")

# Load TF-IDF vectors
resume_vectors = pickle.load(open("models/resume_vectors.pkl", "rb"))
linkedin_vectors = pickle.load(open("models/linkedin_vectors.pkl", "rb"))
naukri_vectors = pickle.load(open("models/naukri_vectors.pkl", "rb"))

print("TF-IDF vectors loaded successfully!")

# Select first resume
resume_index = 0

resume_vector = resume_vectors[resume_index]

print("Selected Resume Category:", resume_df.iloc[resume_index]["Category"])

linkedin_scores = cosine_similarity(
    resume_vector,
    linkedin_vectors
)[0]

naukri_scores = cosine_similarity(
    resume_vector,
    naukri_vectors
)[0]

recommendations = []

top_linkedin = linkedin_scores.argsort()[-5:][::-1]

for idx in top_linkedin:

    recommendations.append({
        "Source": "LinkedIn",
        "Title": linkedin_df.iloc[idx]["title"],
        "Company": "-",
        "Match": round(linkedin_scores[idx] * 100, 2)
    })

    top_naukri = naukri_scores.argsort()[-5:][::-1]

for idx in top_naukri:

    recommendations.append({
        "Source": "Naukri",
        "Title": naukri_df.iloc[idx]["title"],
        "Company": naukri_df.iloc[idx]["company"],
        "Match": round(naukri_scores[idx] * 100, 2)
    })

    recommendations = sorted(
    recommendations,
    key=lambda x: x["Match"],
    reverse=True
)
    
    print("\n========== TOP RECOMMENDED JOBS ==========\n")

for i, job in enumerate(recommendations, start=1):

    print(f"{i}. {job['Title']}")
    print(f"   Source  : {job['Source']}")
    print(f"   Company : {job['Company']}")
    print(f"   Match   : {job['Match']}%")
    print("-" * 40)

    