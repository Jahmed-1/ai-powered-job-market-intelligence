import joblib


model = joblib.load("ml_model/role_classifier_model.pkl")


def predict_job_role(title, description):
    text = title + " " + description

    predicted_role = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities) * 100

    return predicted_role, round(confidence, 2)


if __name__ == "__main__":
    sample_title = "Data Analyst"
    sample_description = """
    We are looking for a Data Analyst with SQL, Python, Excel,
    Power BI, dashboarding, reporting, and data cleaning experience.
    """

    role, confidence = predict_job_role(sample_title, sample_description)

    print("Predicted Role:", role)
    print("Confidence:", confidence, "%")