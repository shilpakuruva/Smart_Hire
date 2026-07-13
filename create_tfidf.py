import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os


# Load LinkedIn jobs
linkedin = pd.read_csv(
    "data/raw/Linkedin_dataset.csv"
)


# Load Naukri jobs
naukri = pd.read_csv(
    "data/raw/naukri.csv"
)


# Rename columns for combining
linkedin = linkedin.rename(
    columns={
        "description": "job_description"
    }
)


naukri = naukri.rename(
    columns={
        "job-description": "job_description"
    }
)


# Select required columns

linkedin_jobs = linkedin[
    ["title", "job_description", "skills"]
]


naukri_jobs = naukri[
    ["title", "job_description", "skills"]
]


# Combine both datasets

jobs = pd.concat(
    [
        linkedin_jobs,
        naukri_jobs
    ],
    ignore_index=True
)


# Fill missing values

jobs["job_description"] = jobs["job_description"].fillna("")

jobs["skills"] = jobs["skills"].fillna("")


# Combine description + skills

jobs["text"] = (
    jobs["job_description"]
    + " "
    + jobs["skills"]
)


print("Total jobs:", len(jobs))


# Create TF-IDF model

tfidf = TfidfVectorizer(
    max_features=5000
)


# Convert jobs into vectors

job_vectors = tfidf.fit_transform(
    jobs["text"]
)


# Create models folder

os.makedirs(
    "models",
    exist_ok=True
)


# Save TF-IDF model

pickle.dump(
    tfidf,
    open(
        "models/tfidf_vectorizer.pkl",
        "wb"
    )
)


# Save job vectors

pickle.dump(
    job_vectors,
    open(
        "models/job_vectors.pkl",
        "wb"
    )
)


# Save job details for displaying results

jobs.to_csv(
    "models/jobs_database.csv",
    index=False
)


print("TF-IDF model created successfully!")