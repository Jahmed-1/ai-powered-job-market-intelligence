import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


df = pd.read_csv("data/filtered_jobs.csv")

df["text"] = df["title"].fillna("") + " " + df["clean_description"].fillna("")
df["label"] = df["predicted_role"]

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model Evaluation:")
print(classification_report(y_test, y_pred, zero_division=0))

joblib.dump(model, "ml_model/role_classifier_model.pkl")

print("Model saved to ml_model/role_classifier_model.pkl")