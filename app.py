import os
import urllib.request
import streamlit as st
import pdfplumber
import plotly.express as px
import re

from ui import (
    load_css,
    show_header,
    show_sidebar,
    show_job_boxes
)
from utils.skill_extractor import extract_skills
from utils.recommend import recommend_jobs

# -------------------------------------------------------------
# AUTOMATED DATA & MODEL DOWNLOAD PIPELINE
# -------------------------------------------------------------
os.makedirs('models', exist_ok=True)
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

def download_from_drive(file_id, save_path):
    if not os.path.exists(save_path):
        print(f"Downloading {save_path} from Google Drive...")
        url = f"https://docs.google.com/uc?export=download&id={file_id}"
        urllib.request.urlretrieve(url, save_path)
        print(f"Successfully downloaded {save_path}!")

# Download heavy structural pipeline dependencies
download_from_drive('1FmmM9IevbDKrJYMD-9iWqU2vQAY4NkUX', 'models/tfidf_vectorizer.pkl')
download_from_drive('1_RUXvP2ynj2gYsmAnmBGuk5Ba9ZO7-oR', 'data/processed/resume_processed.csv')


# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🚀",
    layout="wide"
)

# Initialize global layout components
load_css()
show_header()
show_sidebar()


# --------------------------------
# Resume Cleaning Engine
# --------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# --------------------------------
# Upload Resume Widget
# --------------------------------
uploaded_file = st.file_uploader(
    "",
    type=["pdf"]
)


# --------------------------------
# Main Processing Pipeline
# --------------------------------
if uploaded_file is not None:
    st.success("✅ Resume Uploaded Successfully!")
    resume_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        pages = len(pdf.pages)
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

    clean_resume = clean_text(resume_text)
    words = len(clean_resume.split())
    skills = extract_skills(clean_resume)

    if skills is None:
        skills = []

    # ===============================
    # Analytics Dashboard
    # ===============================
    st.subheader("📊 Dashboard")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🛠 Skills Discovered", len(skills))
    col2.metric("📄 Total Pages", pages)
    col3.metric("📝 Word Count", words)
    col4.metric("💼 Recommended Positions", 10)

    st.divider()

    # ===============================
    # Workflow Pipeline Map
    # ===============================
    st.subheader("🧠 SmartHire AI Workflow")
    st.info("""
📄 Resume Upload  ➡  🧹 Resume Cleaning  ➡  🛠 Skill Extraction  ➡  📊 TF-IDF Vectorization  ➡  🤖 Cosine Similarity Matching  ➡  🎯 Top Job Recommendations
""")

    st.divider()

    # --------------------------------
    # UI Workspace Tabs
    # --------------------------------
    tab1, tab2, tab3 = st.tabs([
        "🛠 Skills Profile",
        "📄 Extracted Data View",
        "🎯 AI Recommendation Engine"
    ])

    # --------------------------------
    # Tab 1: Skills Profile Visualizer
    # --------------------------------
    with tab1:
        st.subheader("Detected Skills")
        if skills:
            cols = st.columns(4)
            for i, skill in enumerate(skills):
                cols[i % 4].success(skill)
        else:
            st.warning("No skills detected. Try utilizing clear formatting or distinct keywords in your resume.")

    # --------------------------------
    # Tab 2: Text Extractor Workspace
    # --------------------------------
    with tab2:
        st.subheader("📄 Extracted Raw Resume Text")
        st.text_area(
            "Raw Text",
            resume_text,
            height=200,
            label_visibility="collapsed"
        )

        st.subheader("🧹 Normalized & Cleaned Text")
        st.text_area(
            "Cleaned Text",
            clean_resume,
            height=200,
            label_visibility="collapsed"
        )

    # --------------------------------
    # Tab 3: Recommendation Processing Workspace
    # --------------------------------
    with tab3:
        if st.button("🚀 Run System Analysis & Find Positions", use_container_width=True):
            with st.spinner("Analyzing profile patterns..."):
                recommendations = recommend_jobs(
                    clean_resume,
                    top_n=10
                )

                if recommendations is None or recommendations.empty:
                    st.error("❌ No matching job profiles found in our indexed matrix.")
                else:
                    # -------------------------------------------------------------
                    # FIXED CRITICAL BUG: Format raw Python array into clean CSV string
                    # -------------------------------------------------------------
                    if "skills" not in recommendations.columns:
                        # Join extracted list tokens with commas so ui.py breaks them up properly
                        formatted_string_skills = ", ".join(skills) if skills else ""
                        recommendations["skills"] = formatted_string_skills
                    else:
                        recommendations["skills"] = recommendations["skills"].astype(str)

                    st.success("✅ Profile Analysis Matrix Evaluated!")
                    st.divider()

                    # Render top-level interactive pie chart and cards sequentially from ui.py
                    show_job_boxes(recommendations)

# --------------------------------
# Page Layout Footer Container
# --------------------------------
st.divider()
st.markdown(
    """
    <div style="text-align:center; padding:20px; color:#64748b;">
        <h4 style="margin-bottom: 5px; color: #2563eb;">🚀 SmartHire AI Platform</h4>
        <p style="font-size: 14px; margin: 0;">AI Powered Resume Screening & Vectorized Recommendation System</p>
        <p style="font-size: 12px; color: #94a3b8; margin-top: 5px;">Built with Python • Streamlit • NLP • Scikit-Learn • Plotly | © 2026 SmartHire AI</p>
    </div>
    """,
    unsafe_allow_html=True
)