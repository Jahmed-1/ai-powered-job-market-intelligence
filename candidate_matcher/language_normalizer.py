def normalize_german_english_terms(text):
    if text is None:
        return ""

    replacements = {
        "datenanalyse": "data analysis",
        "datenanalyst": "data analyst",
        "datenwissenschaft": "data science",
        "datenwissenschaftler": "data scientist",
        "datenbank": "database",
        "datenbanken": "databases",
        "maschinelles lernen": "machine learning",
        "künstliche intelligenz": "artificial intelligence",
        "ki": "artificial intelligence",
        "berichterstattung": "reporting",
        "berichtswesen": "reporting",
        "geschäftsanalyse": "business analysis",
        "datenvisualisierung": "data visualization",
        "dashboard": "dashboard",
        "dashboards": "dashboards",
        "cloud computing": "cloud computing",
        "berufserfahrung": "professional experience",
        "praktische erfahrung": "hands-on experience",
        "kenntnisse": "skills",
        "grundkenntnisse": "basic knowledge",
        "fortgeschrittene kenntnisse": "advanced knowledge",
        "sql kenntnisse": "sql skills",
        "python kenntnisse": "python skills"
    }

    text = text.lower()

    for german_term, english_term in replacements.items():
        text = text.replace(german_term, english_term)

    return text