def extract_skills(text):

    skills_list = [
        "python",
        "java",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "react",
        "javascript",
        "html",
        "css",
        "aws",
        "docker",
        "kubernetes",
        "git",
        "excel",
        "power bi"
    ]
# =========================
# RESUME QUALITY SCORE
# =========================


def resume_score(text, skills):

    score = 0

    text_lower = text.lower()


    # Skills score
    if len(skills) >= 5:
        score += 30
    elif len(skills) >= 3:
        score += 20
    else:
        score += 10



    # Project section
    if "project" in text_lower:
        score += 20



    # Experience section
    if "experience" in text_lower or "internship" in text_lower:
        score += 20



    # Education section
    if "education" in text_lower or "degree" in text_lower:
        score += 15



    # GitHub / LinkedIn
    if "github" in text_lower or "linkedin" in text_lower:
        score += 15



    return min(score,100)

# =========================
# RESUME IMPROVEMENTS
# =========================


def improvement_suggestions(text, skills):

    suggestions=[]

    text=text.lower()


    if len(skills)<5:

        suggestions.append(
            "Add more technical skills relevant to your target job"
        )


    if "project" not in text:

        suggestions.append(
            "Add academic or personal projects"
        )


    if "github" not in text:

        suggestions.append(
            "Add GitHub profile and project links"
        )


    if "internship" not in text:

        suggestions.append(
            "Include internship experience"
        )


    if "certificate" not in text:

        suggestions.append(
            "Add relevant certifications"
        )


    return suggestions


    found_skills = []


    text = text.lower()


    for skill in skills_list:

        if skill in text:

            found_skills.append(skill)


    return found_skills