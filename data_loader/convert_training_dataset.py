import pandas as pd


input_file = "data/training_data/job_postings.csv"
output_file = "data/training_data/job_dataset.csv"


df = pd.read_csv(input_file)

training_df = pd.DataFrame()

training_df["title"] = df["job_title"]
training_df["description"] = df["job_description"]
training_df["label"] = df["job_title"]

training_df = training_df.dropna(subset=["title", "description", "label"])

training_df.to_csv(output_file, index=False)

print("Converted dataset saved to:", output_file)
print("Total training rows:", len(training_df))
print(training_df.head())