
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("fake_job_postings.csv")

features = [
    'title', 'location', 'department', 'salary_range', 'company_profile',
    'description', 'requirements', 'benefits', 'telecommuting',
    'has_company_logo', 'has_questions', 'employment_type',
    'required_experience', 'required_education', 'industry', 'function'
]

df = df[features + ['fraudulent']]
df = df.dropna(subset=['fraudulent'])
df = df.fillna("None")

X = pd.get_dummies(df[features])
y = df['fraudulent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(list(X.columns), open("columns.pkl", "wb"))

print("Model trained and saved successfully.")
