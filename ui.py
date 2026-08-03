import html
import plotly.express as px
import streamlit as st

# -----------------------------
# CSS CONFIGURATION
# -----------------------------
def load_css():
    st.markdown("""
    <style>
    /* Vibrant App Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%) !important;
    }

    /* Force global text readability against dark background (Fixes legend & label visibility) */
    h1, h2, h3, h4, h5, h6, p, span, label, .js-plotly-plot .plotly text {
        color: #f8fafc !important;
    }

    /* Header Main Title Accent */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        background: linear-gradient(90deg, #60a5fa, #c084fc, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1 !important;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Sidebar Base Container */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #070a13 0%, #0d1322 100%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    section[data-testid="stSidebar"] * {
        color: #f8fafc !important;
    }

    /* Modern Radio Group Layout */
    div[data-testid="stSidebar"] div[role="radiogroup"] {
        gap: 6px;
    }

    /* Sidebar Radio Options Styling */
    div[data-testid="stSidebar"] div[role="radiogroup"] label {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 8px 14px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: pointer;
        width: 100%;
    }

    /* Hover State for Unselected Options */
    div[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: rgba(99, 102, 241, 0.12);
        border-color: rgba(99, 102, 241, 0.4);
        transform: translateX(4px);
    }

    /* Selected Radio State (Glowing Active Look) */
    div[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.35) 0%, rgba(168, 85, 247, 0.35) 100%) !important;
        border: 1px solid rgba(168, 85, 247, 0.7) !important;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3);
    }

    /* Hide native radio small dot inputs for a clean button-chip layout */
    div[data-testid="stSidebar"] div[role="radiogroup"] input[type="radio"] {
        display: none;
    }

    /* Text Alignment inside Sidebar Options */
    div[data-testid="stSidebar"] div[role="radiogroup"] div[data-testid="stMarkdownContainer"] p {
        font-size: 14px;
        font-weight: 500;
        letter-spacing: 0.3px;
    }

    /* Primary Action Buttons */
    .stButton button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        border-radius: 14px;
        height: 45px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.6);
    }

    /* Target and Overhaul Streamlit's Native File Uploader (Removes the White Box) */
    [data-testid="stFileUploader"] {
        background-color: rgba(30, 41, 59, 0.85) !important;
        border: 2px dashed #6366f1 !important;
        border-radius: 20px !important;
        padding: 20px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3) !important;
    }
    
    [data-testid="stFileUploader"] section {
        background-color: transparent !important;
    }

    [data-testid="stFileUploader"] section div, 
    [data-testid="stFileUploader"] span, 
    [data-testid="stFileUploader"] small {
        color: #cbd5e1 !important;
    }

    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
    }

    /* Colorful Skill Badge Styling */
    .skill-badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.12);
        color: #93c5fd !important;
        padding: 5px 12px;
        margin: 4px;
        border-radius: 15px;
        font-size: 12px;
        font-weight: 600;
        border: 1px solid rgba(147, 197, 253, 0.3);
        backdrop-filter: blur(5px);
        white-space: normal; 
        word-break: break-word;
    }

    hr {
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------
def show_header():
    st.markdown("""
    <div class="main-title">
        🚀 SmartHire AI Platform
    </div>
    <div class="subtitle">
        AI Powered Resume Screening & Vectorized Recommendation System
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# UPLOAD SECTION
# -----------------------------
def upload_section():
    st.markdown("""
    <div style="
        background: rgba(30, 41, 59, 0.6);
        padding: 10px 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 5px;
    ">
        <h3 style="color: #60a5fa !important; margin: 0px 0px 4px 0px;">
            📂 Upload Your Resume Below
        </h3>
        <p style="color: #94a3b8 !important; font-size: 13px; margin: 0px;">
            Supports PDF format. SmartHire AI will immediately process your text and extract relevant features.
        </p>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------
# SIDEBAR
# -----------------------------
def show_sidebar():
    st.sidebar.image("assets/logo.png", width=110)
    st.sidebar.markdown("<h2 style='text-align:center; color:#60a5fa !important;'>SmartHire AI</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("---")
    st.sidebar.subheader("📌 Navigation")

    menu_options = [
        "🏠 Dashboard",
        "📄 Resume Upload", 
        "🧹 Resume Cleaning",
        "🛠 Skill Extraction",
        "🤖 AI Job Matching", 
        "📊 Resume Analytics", 
        "🎯 Job Recommendations",
        "💼 Cards Matched",
        "📚 Skills Learn",
        "📍 Job Locations"
    ]
    
    selected_page = st.sidebar.radio("Go to", menu_options, label_visibility="collapsed")
    st.session_state.page = selected_page

    st.sidebar.markdown("---")
    st.sidebar.subheader("⚙️ AI Pipeline")

    pipeline = [
        "📄 PDF Resume", "🧹 Text Cleaning", "🛠 Skill Extraction",
        "📊 TF-IDF Vectorization", "🤖 Cosine Similarity", "🎯 Job Ranking"
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
""")
    st.sidebar.markdown("---")
    st.sidebar.success("🚀 SmartHire AI v1.0")
    st.sidebar.caption("Built with ❤️ using Streamlit")


# -----------------------------
# FEATURE VIEW: CARDS MATCHED
# -----------------------------
def show_cards_matched():
    st.subheader("💼 Cards Matched History")
    st.info("Here you can review all the job card matches saved from your previous screening sessions.")
    st.markdown("*(Your matched job card history records will appear here)*")


# -----------------------------
# FEATURE VIEW: SKILLS LEARN
# -----------------------------
def show_skills_learn():
    st.subheader("📚 Skills to Learn & Master")
    st.markdown("<p style='color:#cbd5e1;'>Bridge your skill gaps with curated learning roadmaps recommended by SmartHire AI.</p>", unsafe_allow_html=True)
    
    skill_categories = [
        {"title": "🐍 Advanced Python & APIs", "level": "Intermediate", "duration": "3 Weeks", "desc": "Master decorators, generators, async programming, and FastAPI development.", "bg": "linear-gradient(135deg, #1e1b4b, #312e81)", "border": "#6366f1"},
        {"title": "🐳 Docker & Kubernetes", "level": "Advanced", "duration": "4 Weeks", "desc": "Learn containerization, microservices deployment, and cluster orchestration.", "bg": "linear-gradient(135deg, #064e3b, #065f46)", "border": "#10b981"},
        {"title": "☁️ AWS Cloud Practitioner", "level": "Beginner", "duration": "5 Weeks", "desc": "Understand EC2, S3, IAM policies, serverless functions, and cloud security.", "bg": "linear-gradient(135deg, #78350f, #92400e)", "border": "#f59e0b"},
        {"title": "📊 Advanced SQL & Data Pipelines", "level": "Intermediate", "duration": "2 Weeks", "desc": "Optimize queries, handle window functions, and design data warehouses.", "bg": "linear-gradient(135deg, #831843, #9d174d)", "border": "#ec4899"}
    ]

    cols = st.columns(2)
    for i, cat in enumerate(skill_categories):
        with cols[i % 2]:
            card_html = f"""
            <div style="
                background: {cat['bg']};
                border-radius: 20px;
                padding: 24px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.4);
                margin-bottom: 20px;
                border-left: 6px solid {cat['border']};
                border: 1px solid rgba(255,255,255,0.1);
            ">
                <h4 style="color: #ffffff !important; margin-top: 0px; margin-bottom: 8px;">{cat['title']}</h4>
                <div style="display: flex; gap: 10px; margin-bottom: 12px;">
                    <span style="background: rgba(255,255,255,0.2); color: #ffffff; padding: 4px 10px; border-radius: 10px; font-size: 11px; font-weight: bold;">Level: {cat['level']}</span>
                    <span style="background: rgba(0,0,0,0.3); color: #a7f3d0; padding: 4px 10px; border-radius: 10px; font-size: 11px; font-weight: bold;">Duration: {cat['duration']}</span>
                </div>
                <p style="color: #e2e8f0 !important; font-size: 13px; margin-bottom: 0px;">{cat['desc']}</p>
            </div>
            """
            st.html(card_html)
            if st.button("Start Learning Roadmap", key=f"learn_{i}", use_container_width=True):
                st.success(f"Enrolled in roadmap for: {cat['title']}")


# -----------------------------
# FEATURE VIEW: JOB LOCATIONS
# -----------------------------
def show_job_locations():
    st.subheader("📍 Job Locations & Regional Hubs")
    st.markdown("<p style='color:#cbd5e1;'>Explore open positions categorized by geographic region and remote flexibility.</p>", unsafe_allow_html=True)
    
    locations = [
        {"city": "🌐 Remote / Work From Home", "openings": "1,420 Active Roles", "top_tech": "Fullstack, Python, React, DevOps", "bg": "linear-gradient(135deg, #1e3a8a, #1e40af)", "border": "#3b82f6"},
        {"city": "🇮🇳 Bangalore, India", "openings": "850 Active Roles", "top_tech": "Java, Spring Boot, Data Science, AWS", "bg": "linear-gradient(135deg, #581c87, #6b21a8)", "border": "#a855f7"},
        {"city": "🇮🇳 Hyderabad, India", "openings": "610 Active Roles", "top_tech": "Python, SQL, Cloud Computing, QA", "bg": "linear-gradient(135deg, #14532d, #166534)", "border": "#22c55e"},
        {"city": "🇺🇸 San Francisco, USA", "openings": "980 Active Roles", "top_tech": "AI/ML, System Architecture, Go, Kubernetes", "bg": "linear-gradient(135deg, #7f1d1d, #991b1b)", "border": "#ef4444"}
    ]

    cols = st.columns(2)
    for i, loc in enumerate(locations):
        with cols[i % 2]:
            loc_card = f"""
            <div style="
                background: {loc['bg']};
                border-radius: 20px;
                padding: 24px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.4);
                margin-bottom: 20px;
                border-top: 6px solid {loc['border']};
                border: 1px solid rgba(255,255,255,0.1);
            ">
                <h4 style="color: #ffffff !important; margin-top: 0px; margin-bottom: 6px;">{loc['city']}</h4>
                <p style="color: #6ee7b7 !important; font-weight: bold; font-size: 14px; margin-bottom: 6px;">📈 {loc['openings']}</p>
                <p style="color: #cbd5e1 !important; font-size: 12px; margin-bottom: 0px;"><b>Trending Skills:</b> {loc['top_tech']}</p>
            </div>
            """
            st.html(loc_card)
            if st.button(f"Filter Jobs in {loc['city'].split(' ')[-1]}", key=f"loc_{i}", use_container_width=True):
                st.success(f"Filtered matches for location: {loc['city']}")


# -----------------------------
# JOB CARDS RENDER PIPELINE
# -----------------------------
def show_job_boxes(recommendations):
    st.subheader("🎯 Top Job Recommendations")

    if not recommendations.empty:
        chart_data = recommendations.head(10)  
        
        fig = px.pie(
            chart_data, 
            values='match_score', 
            names='title', 
            title='Match Distribution Strength (Top Results)',
            hole=0.4, 
            color_discrete_sequence=px.colors.sequential.Sunset  
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="sans-serif", size=12, color="#f8fafc"),
            title_font=dict(size=16, color="#60a5fa", family="sans-serif")
        )
        
        with st.container():
            st.markdown('<div style="background: rgba(30, 41, 59, 0.8); padding: 15px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); margin-bottom: 25px; border: 1px solid rgba(255,255,255,0.1);">', unsafe_allow_html=True)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    cols = st.columns(3)

    for i, (_, row) in enumerate(recommendations.iterrows()):
        score = float(row["match_score"])
        title = str(row["title"])

        if len(title) > 45:
            title = title[:45] + "..."

        skills = row.get("skills", "")
        skill_list = []

        if skills is not None:
            if isinstance(skills, list):
                skill_list = skills
            else:
                skills = str(skills).strip()
                if skills.lower() not in ["nan", "none", ""]:
                    skills = (
                        skills
                        .replace("[","")
                        .replace("]","")
                        .replace("'","")
                        .replace('"',"")
                    )
                    if "," in skills:
                        skill_list = skills.split(",")
                    else:
                        skill_list = skills.split()

        skill_list = [skill.strip() for skill in skill_list if skill.strip()]
        skill_list = list(dict.fromkeys(skill_list)) 
        skill_list = skill_list[:4]                 

        if skill_list:
            badges = ""
            for skill in skill_list:
                skill = html.escape(str(skill))
                badges += f'<span class="skill-badge">{skill}</span>\n'
        else:
            badges = '<span class="skill-badge" style="background:rgba(255,255,255,0.05); color:#94a3b8;">No Skills Specified</span>'

        with cols[i % 3]:
            safe_title = html.escape(title)

            card_html = f"""
            <div style="
                background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.95));
                border-radius: 20px;
                padding: 20px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.4);
                min-height: 330px;
                text-align: center;
                margin-bottom: 20px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                border: 1px solid rgba(255,255,255,0.1);
            ">
                <div>
                    <h4 style="
                        color: #60a5fa !important;
                        font-size: 16px;
                        font-weight: 600;
                        height: 50px;
                        overflow: hidden;
                        margin-top: 0px;
                    ">
                        💼 {safe_title}
                    </h4>

                    <div style="
                        font-size: 32px;
                        font-weight: bold;
                        color: #4ade80 !important;
                        text-shadow: 0 0 10px rgba(74, 222, 128, 0.3);
                    ">
                        {score:.1f}%
                    </div>

                    <p style="
                        color: #94a3b8 !important;
                        font-size: 13px;
                        margin-top: 5px;
                        margin-bottom: 10px;
                    ">
                        Match Score
                    </p>
                </div>

                <div style="
                    margin-top: 10px;
                    margin-bottom: 10px;
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 4px;
                    min-height: 60px;
                ">
                    {badges}
                </div>
            </div>
            """

            st.html(card_html)
            st.progress(score / 100)

            if st.button("Apply Now", key=f"apply_{i}", use_container_width=True):
                st.success(f"Application started for {title}")