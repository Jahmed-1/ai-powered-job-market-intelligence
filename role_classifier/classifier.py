def classify_role(title, description):
    text = f"{title} {description}".lower()

    if any(word in text for word in ["ai engineer", "ml engineer", "computer vision", "generative ai", "ai automation"]):
        return "AI/ML Engineer"

    elif any(word in text for word in ["data analyst", "datenanalyse", "power bi", "tableau", "excel"]):
        return "Data Analyst"

    elif any(word in text for word in ["data scientist", "data science", "machine learning", "deep learning"]):
        return "Data Scientist"

    elif any(word in text for word in ["data engineer", "etl", "pipeline", "spark", "airflow"]):
        return "Data Engineer"

    elif any(word in text for word in ["aws", "azure", "cloud", "devops"]):
        return "Cloud Engineer"

    elif any(word in text for word in ["database", "oracle", "sql", "java"]):
        return "Database/Backend Role"

    else:
        return "Other Technical Role"