import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

df = pd.read_csv('ml/train.csv')

model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

model.fit(df['task_description'], df['priority'])

joblib.dump(model, 'ml/task_model.joblib')

print("Model trained and saved to ml/task_model.joblib")
