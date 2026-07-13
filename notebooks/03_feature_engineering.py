import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load processed datasets
resume_df = pd.read_csv("data/processed/resume_processed.csv")
linkedin_df = pd.read_csv("data/processed/linkedin_processed.csv")
naukri_df = pd.read_csv("data/processed/naukri_processed.csv")

print("Processed datasets loaded successfully!")

# Check missing values
print("\nMissing values:")
print("Resume:", resume_df["clean_resume"].isnull().sum())
print("LinkedIn:", linkedin_df["clean_job"].isnull().sum())
print("Naukri:", naukri_df["clean_job"].isnull().sum())

# Replace NaN with empty strings
resume_df["clean_resume"] = resume_df["clean_resume"].fillna("")
linkedin_df["clean_job"] = linkedin_df["clean_job"].fillna("")
naukri_df["clean_job"] = naukri_df["clean_job"].fillna("")

# Create TF-IDF Vectorizer
tfidf = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

# Resume vectors
resume_vectors = tfidf.fit_transform(resume_df["clean_resume"])
print("Resume TF-IDF Shape:", resume_vectors.shape)

# LinkedIn vectors
linkedin_vectors = tfidf.transform(linkedin_df["clean_job"])
print("LinkedIn TF-IDF Shape:", linkedin_vectors.shape)

# Naukri vectors
naukri_vectors = tfidf.transform(naukri_df["clean_job"])
print("Naukri TF-IDF Shape:", naukri_vectors.shape)

# Save models
pickle.dump(tfidf, open("models/tfidf.pkl", "wb"))
pickle.dump(resume_vectors, open("models/resume_vectors.pkl", "wb"))
pickle.dump(linkedin_vectors, open("models/linkedin_vectors.pkl", "wb"))
pickle.dump(naukri_vectors, open("models/naukri_vectors.pkl", "wb"))

print("TF-IDF vectors saved successfully!")