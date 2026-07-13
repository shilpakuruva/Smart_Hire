import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load processed datasets
# -----------------------------
resume_df = pd.read_csv("data/processed/resume_processed.csv")
linkedin_df = pd.read_csv("data/processed/linkedin_processed.csv")
naukri_df = pd.read_csv("data/processed/naukri_processed.csv")

print("Datasets loaded successfully!")

# -----------------------------
# Load TF-IDF vectors
# -----------------------------
resume_vectors = pickle.load(open("models/resume_vectors.pkl", "rb"))
linkedin_vectors = pickle.load(open("models/linkedin_vectors.pkl", "rb"))
naukri_vectors = pickle.load(open("models/naukri_vectors.pkl", "rb"))

print("TF-IDF vectors loaded successfully!")

# -----------------------------
# Select a resume
# -----------------------------
resume_index = 0

print("\nResume Category:")
print(resume_df.iloc[resume_index]["Category"])

# Get vector of selected resume
resume_vector = resume_vectors[resume_index]

# -----------------------------
# LinkedIn Similarity
# -----------------------------
linkedin_similarity = cosine_similarity(
    resume_vector,
    linkedin_vectors
)[0]

top_linkedin = linkedin_similarity.argsort()[-5:][::-1]

print("\n========== TOP 5 LINKEDIN JOBS ==========\n")

for idx in top_linkedin:

    print("Title :", linkedin_df.iloc[idx]["title"])
    print("Match :", round(linkedin_similarity[idx] * 100, 2), "%")
    print()

# -----------------------------
# Naukri Similarity
# -----------------------------
naukri_similarity = cosine_similarity(
    resume_vector,
    naukri_vectors
)[0]

top_naukri = naukri_similarity.argsort()[-5:][::-1]

print("\n========== TOP 5 NAUKRI JOBS ==========\n")

for idx in top_naukri:

    print("Title :", naukri_df.iloc[idx]["title"])
    print("Company :", naukri_df.iloc[idx]["company"])
    print("Match :", round(naukri_similarity[idx] * 100, 2), "%")
    print()

print("Resume Matching Completed Successfully!")