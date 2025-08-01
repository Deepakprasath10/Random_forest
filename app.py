from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)

# Load model and columns
model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    for col in columns:
        if col not in data:
            data[col] = "None"

    df = pd.DataFrame([data])
    df_encoded = pd.get_dummies(df)
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df_encoded)[0]
    result = "Fake Job Posting ❌" if prediction == 1 else "Legit Job Posting ✅"

    return render_template("index.html", prediction=result)

# 👇 THIS MUST BE INCLUDED
if __name__ == '__main__':
    app.run(debug=True)
