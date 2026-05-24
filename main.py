from data_loader.arbeitnow_loader import fetch_arbeitnow_jobs
from preprocessing.text_cleaner import clean_text
from preprocessing.job_filter import filter_data_jobs
from skill_extractor.extractor import extract_skills
from skill_extractor.skill_analyzer import count_skills
from role_classifier.classifier import classify_role
from role_classifier.role_analyzer import count_roles
from ml_model.predict_role import predict_job_role
import pandas as pd


df = fetch_arbeitnow_jobs()
df["clean_description"] = df["description"].apply(clean_text)
filtered_df = filter_data_jobs(df)
filtered_df["extracted_skills"] = filtered_df["clean_description"].apply(extract_skills)
filtered_df["predicted_role"] = filtered_df.apply(
    lambda row: classify_role(row["title"], row["clean_description"]),
    axis=1
)
filtered_df[["ml_predicted_role", "ml_confidence"]] = filtered_df.apply(
    lambda row: pd.Series(
        predict_job_role(row["title"], row["clean_description"])
    ),
    axis=1
)

role_counts = count_roles(filtered_df["predicted_role"])
role_df = pd.DataFrame(
    role_counts.items(),
    columns=["role", "count"]
)
role_df = role_df.sort_values(by="count", ascending=False)
role_df.to_csv("data/top_roles.csv", index=False)

print("Top job roles:")
for role, count in role_counts.items():
    print(f"{role}: {count}")
skill_counts = count_skills(filtered_df["extracted_skills"])
skill_df = pd.DataFrame(
    skill_counts.items(),
    columns=["skill", "count"]
)

skill_df = skill_df.sort_values(by="count", ascending=False)
filtered_df.to_csv("data/filtered_jobs.csv", index=False)
skill_df.to_csv("data/top_skills.csv", index=False)

print(
    filtered_df[
        [
            "title",
            "predicted_role",
            "ml_predicted_role",
            "ml_confidence",
            "extracted_skills",
        ]
    ].head(10).to_string()
)
print("Top demanded skills:")
for skill, count in skill_counts.items():
    print(f"{skill}: {count}")
print("Total jobs before filtering:", len(df))
print("Total relevant jobs after filtering:", len(filtered_df))