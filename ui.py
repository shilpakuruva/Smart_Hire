import streamlit as st
import html


# -----------------------------
# CSS
# -----------------------------
def load_css():

    st.markdown("""
    <style>

    .stApp{
        background:linear-gradient(135deg,#eef2ff,#f8fafc);
    }


    /* Header */

    .main-title{
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:#2563eb;
        margin-bottom:0px;
    }


    .subtitle{
        text-align:center;
        color:#6b7280;
        font-size:18px;
        margin-bottom:30px;
    }


    /* Sidebar */

    section[data-testid="stSidebar"]{
        background:#1e293b;
    }


    section[data-testid="stSidebar"] *{
        color:white;
    }



    /* Buttons */

    .stButton button{

        background:#2563eb;
        color:white;
        border-radius:12px;
        height:45px;
        font-weight:bold;

    }


    .stButton button:hover{

        background:#1d4ed8;

    }



    /* Skill Badge */

    .skill-badge{

        display:inline-block;
        background:#dbeafe;
        color:#2563eb;
        padding:5px 10px;
        margin:3px;
        border-radius:15px;
        font-size:12px;
        font-weight:600;
        white-space: normal; /* FIX: Allows long text inside badges to wrap gracefully */
        word-break: break-word;

    }



    hr{

        border:1px solid #e5e7eb;

    }


    </style>
    """, unsafe_allow_html=True)



# -----------------------------
# HEADER
# -----------------------------
def show_header():

    st.markdown("""
    <div class="main-title">
        🚀 SmartHire AI
    </div>

    <div class="subtitle">
        AI Powered Resume Screening & Job Recommendation Platform
    </div>
    """, unsafe_allow_html=True)



# -----------------------------
# UPLOAD SECTION
# -----------------------------
def upload_section():

    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0 4px 10px rgba(0,0,0,.1);
        text-align:center;
        margin-bottom:20px;
    ">

        <h2 style="color:#2563eb;">
            📂 Upload Your Resume
        </h2>

        <p style="color:#6b7280;">
            Upload your PDF resume and let SmartHire AI analyze your skills
            and recommend the best matching jobs.
        </p>

    </div>
    """, unsafe_allow_html=True)



# -----------------------------
# SIDEBAR
# -----------------------------
def show_sidebar():

    st.sidebar.image(
        "assets/logo.png",
        width=110
    )


    st.sidebar.markdown(
        "<h2 style='text-align:center;'>SmartHire AI</h2>",
        unsafe_allow_html=True
    )


    st.sidebar.markdown("---")


    st.sidebar.subheader("📌 Navigation")


    menu = [

        "🏠 Dashboard",
        "📄 Resume Upload",
        "🧹 Resume Cleaning",
        "🛠 Skill Extraction",
        "🤖 AI Job Matching",
        "📊 Resume Analytics",
        "🎯 Job Recommendations"

    ]


    for item in menu:

        st.sidebar.success(item)



    st.sidebar.markdown("---")


    st.sidebar.subheader("⚙️ AI Pipeline")


    pipeline = [

        "📄 PDF Resume",
        "🧹 Text Cleaning",
        "🛠 Skill Extraction",
        "📊 TF-IDF Vectorization",
        "🤖 Cosine Similarity",
        "🎯 Job Ranking"

    ]


    for step in pipeline:

        st.sidebar.info(step)



    st.sidebar.markdown("---")


    st.sidebar.subheader("💻 Technologies")


    st.sidebar.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 🧠 NLP
- 📊 Plotly
- 🤖 Scikit-Learn
- 📑 PDFPlumber
- 🔍 TF-IDF
- 📐 Cosine Similarity
""")


    st.sidebar.markdown("---")


    st.sidebar.success(
        "🚀 SmartHire AI v1.0"
    )


    st.sidebar.caption(
        "Built with ❤️ using Streamlit"
    )



# -----------------------------
# JOB CARDS
# -----------------------------
def show_job_boxes(recommendations):

    st.subheader("🎯 Top Job Recommendations")

    cols = st.columns(3)

    for i, (_, row) in enumerate(recommendations.iterrows()):

        score = float(row["match_score"])
        title = str(row["title"])

        if len(title) > 45:
            title = title[:45] + "..."

        # -----------------------------
        # Skills Handling
        # -----------------------------
        skills = row.get("skills", "")
        skill_list = []

        if skills is not None:
            if isinstance(skills, list):
                skill_list = skills
            else:
                skills = str(skills)
                if skills.lower() not in ["nan", "none", ""]:
                    skills = (
                        skills
                        .replace("[","")
                        .replace("]","")
                        .replace("'","")
                        .replace('"',"")
                    )
                    skill_list = skills.split(",")

        skill_list = [
            skill.strip()
            for skill in skill_list
            if skill.strip()
        ]

        # remove duplicates
        skill_list = list(dict.fromkeys(skill_list))

        # maximum 4 skills
        skill_list = skill_list[:4]


        # -----------------------------
        # Create Badges
        # -----------------------------
        if skill_list:
            badges = ""
            for skill in skill_list:
                skill = html.escape(str(skill))
                badges += f'<span class="skill-badge">{skill}</span>\n'
        else:
            badges = '<span class="skill-badge">No Skills</span>'


        # -----------------------------
        # Card UI
        # -----------------------------
        with cols[i % 3]:
            safe_title = html.escape(title)

            card_html = f"""
            <div style="
                background:white;
                border-radius:18px;
                padding:18px;
                box-shadow:0 5px 15px rgba(0,0,0,.12);
                min-height:300px;
                text-align:center;
                margin-bottom:20px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            ">
                <div>
                    <h4 style="
                        color:#2563eb;
                        font-size:16px;
                        font-weight:600;
                        height:50px;
                        overflow:hidden;
                        margin-top:0px;
                    ">
                        💼 {safe_title}
                    </h4>

                    <div style="
                        font-size:30px;
                        font-weight:bold;
                        color:#16a34a;
                    ">
                        {score:.1f}%
                    </div>

                    <p style="
                        color:#666;
                        font-size:14px;
                        margin-top:5px;
                        margin-bottom:10px;
                    ">
                        Match Score
                    </p>
                </div>

                <div style="
                    margin-top:10px;
                    margin-bottom:10px;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 4px;
                    min-height:60px;
                ">
                    {badges}
                </div>
            </div>
            """

            st.html(card_html)

            st.progress(score / 100)

            if st.button(
                "Apply Now",
                key=f"apply_{i}",
                use_container_width=True
            ):
                st.success(f"Application started for {title}")