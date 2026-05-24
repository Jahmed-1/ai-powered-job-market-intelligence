def map_role_label(raw_label):
    if raw_label is None:
        return "Other Technical Role"

    label = str(raw_label).lower()

    if any(word in label for word in ["data analyst", "business analyst", "bi analyst", "bi developer", "reporting analyst"]):
        return "Data Analyst"

    elif any(word in label for word in ["data scientist", "research scientist", "analytics scientist"]):
        return "Data Scientist"

    elif any(word in label for word in ["data engineer", "etl developer", "big data engineer", "pipeline engineer"]):
        return "Data Engineer"

    elif any(word in label for word in ["machine learning", "ml engineer", "ai engineer", "computer vision", "nlp engineer"]):
        return "AI/ML Engineer"

    elif any(word in label for word in ["cloud engineer", "aws", "azure", "devops", "cloud developer"]):
        return "Cloud Engineer"

    elif any(word in label for word in ["database", "backend", "software engineer", "java developer", "sql developer"]):
        return "Database/Backend Role"

    else:
        return "Other Technical Role"