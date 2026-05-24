import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from data_loader.training_dataset_loader import load_training_dataset
from ml_model.label_mapper import map_role_label


df = load_training_dataset("data/training_data/job_dataset.csv")

df["mapped_label"] = df["label"].apply(map_role_label)

df = df[df["mapped_label"] != "Other Technical Role"]

X = df["text"]
y = df["mapped_label"]

print("Training samples:", len(df))
print("Role distribution:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=10000, stop_words="english")),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=0))

joblib.dump(model, "ml_model/role_classifier_model.pkl")

print("\nModel saved to ml_model/role_classifier_model.pkl")