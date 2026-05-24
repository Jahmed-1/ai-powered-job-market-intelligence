import pandas as pd


def load_training_dataset(file_path="data/training_data/job_dataset.csv"):
    df = pd.read_csv(file_path)

    required_columns = ["title", "description", "label"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    df = df.dropna(subset=["title", "description", "label"])

    df["text"] = df["title"].fillna("") + " " + df["description"].fillna("")

    return df