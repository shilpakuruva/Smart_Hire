from ui import (
    load_css,
    show_header,
    show_sidebar,
    show_job_boxes
)

import streamlit as st
import pdfplumber
import plotly.express as px
import re

from utils.skill_extractor import extract_skills
from utils.recommend import recommend_jobs


# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="SmartHire AI",
    page_icon="🚀",
    layout="wide"
)

load_css()
show_header()
show_sidebar()



# --------------------------------
# Resume Cleaning
# --------------------------------
def clean_text(text):

    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------
# Upload Resume
# --------------------------------
uploaded_file = st.file_uploader(
    "",
    type=["pdf"]
)


# --------------------------------
# Process Resume
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
    # Dashboard
    # ===============================

    st.subheader("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🛠 Skills", len(skills))
    col2.metric("📄 Pages", pages)
    col3.metric("📝 Words", words)
    col4.metric("💼 Recommended Jobs", 10)

    st.divider()

    # ===============================
    # Workflow
    # ===============================

    st.subheader("🧠 SmartHire AI Workflow")

    st.info("""
📄 Resume Upload

⬇

🧹 Resume Cleaning

⬇

🛠 Skill Extraction

⬇

📊 TF-IDF Vectorization

⬇

🤖 Cosine Similarity Matching

⬇

🎯 Top Job Recommendations
""")

    st.divider()


    # --------------------------------
    # Tabs
    # --------------------------------

    tab1, tab2, tab3 = st.tabs([
        "🛠 Skills",
        "📄 Resume",
        "🎯 Job Recommendations"
    ])



    # --------------------------------
    # Skills Tab
    # --------------------------------

    with tab1:

        st.subheader("Detected Skills")


        if skills:

            cols = st.columns(4)

            for i, skill in enumerate(skills):

                cols[i % 4].success(skill)

        else:

            st.warning("No skills detected.")



    # --------------------------------
    # Resume Tab
    # --------------------------------

    with tab2:

        st.subheader("📄 Extracted Resume")


        st.text_area(
            "",
            resume_text,
            height=250
        )


        st.subheader("🧹 Clean Resume")


        st.text_area(
            "",
            clean_resume,
            height=250
        )



    # --------------------------------
    # Job Recommendation Tab
    # --------------------------------

    with tab3:


        if st.button(
            "🚀 Analyze & Find Jobs",
            use_container_width=True
        ):


            with st.spinner("Analyzing Resume..."):


                recommendations = recommend_jobs(
                    clean_resume,
                    top_n=10
                )


                if recommendations is None or recommendations.empty:

                    st.error(
                        "❌ No job recommendations found."
                    )


                else:


                    # Add skills to job cards

                    if "skills" not in recommendations.columns:

                        recommendations["skills"] = recommendations["title"].apply(
                            lambda x: skills
                        )



                    st.success(
                        "✅ Analysis Completed Successfully!"
                    )


                    st.divider()


                    # Job Cards

                    show_job_boxes(
                        recommendations
                    )


    

# --------------------------------
# Footer
# --------------------------------

st.divider()

st.markdown(
    """
<div style="text-align:center;padding:20px;color:gray">

<h4>🚀 SmartHire AI</h4>

AI Powered Resume Screening & Job Recommendation System

Built using ❤️ Python • Streamlit • NLP • Scikit-Learn • Plotly

© 2026 SmartHire AI

</div>
""",
    unsafe_allow_html=True
)