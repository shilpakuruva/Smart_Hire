import os
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Check which file is running
# ==========================================
print("=" * 50)
print("SMART HIRE - RECOMMENDATION SYSTEM")
print("Running File:", os.path.abspath(__file__))
print("=" * 50)

# ==========================================
# Load Processed Datasets
# ==========================================
resume_df = pd.read_csv("data/processed/resume_processed.csv")
linkedin_df = pd.read_csv("data/processed/linkedin_processed.csv")
naukri_df = pd.read_csv("data/processed/naukri_processed.csv")

print("\nDatasets loaded successfully!")

# ==========================================
# Load TF-IDF Vectors
# ==========================================
resume_vectors = pickle.load(open("models/resume_vectors.pkl", "rb"))
linkedin_vectors = pickle.load(open("models/linkedin_vectors.pkl", "rb"))
naukri_vectors = pickle.load(open("models/naukri_vectors.pkl", "rb"))

print("TF-IDF vectors loaded successfully!")

# ==========================================
# Select Resume
# ==========================================
resume_index = 0
resume_vector = resume_vectors[resume_index]

print("\nSelected Resume Category:", resume_df.iloc[resume_index]["Category"])

# ==========================================
# Calculate Similarity
# ==========================================
linkedin_scores = cosine_similarity(
    resume_vector,
    linkedin_vectors
)[0]

naukri_scores = cosine_similarity(
    resume_vector,
    naukri_vectors
)[0]

# ==========================================
# Store Recommendations
# ==========================================
recommendations = []

# LinkedIn Top 5
top_linkedin = linkedin_scores.argsort()[-5:][::-1]

for idx in top_linkedin:
    recommendations.append({
        "Source": "LinkedIn",
        "Title": linkedin_df.iloc[idx]["title"],
        "Company": "-",
        "Match": round(linkedin_scores[idx] * 100, 2)
    })

# Naukri Top 5
top_naukri = naukri_scores.argsort()[-5:][::-1]

for idx in top_naukri:
    recommendations.append({
        "Source": "Naukri",
        "Title": naukri_df.iloc[idx]["title"],
        "Company": naukri_df.iloc[idx]["company"],
        "Match": round(naukri_scores[idx] * 100, 2)
    })

# ==========================================
# Sort Recommendations
# ==========================================
recommendations.sort(
    key=lambda x: x["Match"],
    reverse=True
)

# ==========================================
# Print Results
# ==========================================
print("\n" + "=" * 50)
print("TOP 10 RECOMMENDED JOBS")
print("=" * 50)

for i, job in enumerate(recommendations[:10], start=1):

    print(f"\n{i}. {job['Title']}")
    print(f"Source  : {job['Source']}")
    print(f"Company : {job['Company']}")
    print(f"Match   : {job['Match']}%")
    print("-" * 50)

print("\nRecommendation System Completed Successfully!")