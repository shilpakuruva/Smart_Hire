# 🚀 SmartHire AI Platform

SmartHire AI is an advanced, automated resume screening and career recommendation dashboard built using Python, Streamlit, and Vectorized Natural Language Processing (NLP). 

---

## 🧠 System Architecture & Workflow
The platform processes candidate profiles through a structured, multi-stage machine learning pipeline:

1. **Resume Ingestion (PDF):** Extracts raw text data dynamically from uploaded multi-page PDF profiles using `pdfplumber`.
2. **Text Normalization:** Sanitizes, lowers, and cleans input datasets using advanced regex text normalization patterns.
3. **Skill Discovery:** Runs tokens through an explicit text analyzer to isolate professional capabilities.
4. **TF-IDF Vectorization & Cosine Similarity:** Transforms sparse textual variables into numerical matrix representations, analyzing distance weights against the profile database.
5. **Deduplication Engine:** Evaluates broad categorical clusters dynamically to eliminate repeating tracks and guarantee unique domain recommendation variants.
6. **Skill Gap Analytics:** Benchmarks user skills against extracted text parameters to dynamically offer upskilling suggestions.
7. **Reporting Framework:** Packages career tracking details into a clean, downloadable analytical CSV structure.

---

## 📊 App Workspace Showcase
* **Dashboard Metrics Panel:** Instantly evaluates word count, file structure, page parameters, and aggregate match recommendations.
* **Interactive Data Views:** Offers comparative side-by-side fields viewing parsed text vs. clean regex-normalized strings.
* **Skill Matrix:** Isolates and tags discoverable professional competencies.

---

## 🛠️ Tech Stack & Dependencies
* **Frontend UI Layout:** Streamlit Engine, custom HTML5/CSS vector layout styles, Plotly Express
* **NLP & Analytical Matching:** Scikit-Learn (TF-IDF Vectorizer Matrix), Re, PDFPlumber
* **Data Processing Layer:** Pandas DataFrames, Pickle Serialization Architecture