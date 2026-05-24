def extract_skills(text):
    skills = [
        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "machine learning",
        "deep learning",
        "data science",
        "data analysis",
        "aws",
        "azure",
        "cloud",
        "database",
        "oracle",
        "java",
        "etl",
        "api",
        "pandas",
        "numpy",
        "scikit-learn"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills