def filter_data_jobs(df):
    keywords = [
        "data analyst",
        "data scientist",
        "data engineer",
        "business intelligence",
        "bi analyst",
        "machine learning",
        "ml engineer",
        "ai engineer",
        "data science",

        "python",
        "sql",
        "database",
        "oracle",
        "java",
        "cloud",
        "aws",
        "azure",
        "etl",
        "power bi",
        "tableau",

        "datenanalyse",
        "datenbank",
        "künstliche intelligenz",
        "maschinelles lernen",
        "cloud computing"
    ]

    pattern = "|".join(keywords)

    filtered_df = df[
        df["title"].str.lower().str.contains(pattern, na=False) |
        df["clean_description"].str.lower().str.contains(pattern, na=False)
    ]

    return filtered_df