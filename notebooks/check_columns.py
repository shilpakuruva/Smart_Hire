import pandas as pd

linkedin_df = pd.read_csv("data/processed/linkedin_processed.csv")
print("LinkedIn columns:")
print(linkedin_df.columns.tolist())

naukri_df = pd.read_csv("data/processed/naukri_processed.csv")
print("\nNaukri columns:")
print(naukri_df.columns.tolist())

resume_df = pd.read_csv("data/processed/resume_processed.csv")
print("\nResume columns:")
print(resume_df.columns.tolist())