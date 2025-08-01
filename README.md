
#  Fake Job Posting Detector

A machine learning web application that predicts whether a job posting is **legitimate or fake** using a **Random Forest Classifier**, built with **Flask**.

---

##  Features

-  Detects fake job listings based on textual input
-  Trained on labeled dataset using Random Forest Classifier
-  Flask-based responsive web interface
-  Supports manual model retraining
-  Custom UI with CSS

---

##  Project Structure

```
fake-job-detector/
├── app.py                # Main Flask web application
├── model_train.py        # Script to train and save the ML model
├── job_model.pkl         # Pre-trained Random Forest model
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Custom styles
├── templates/
│   ├── index.html        # Form page for job details
│   └── result.html       # Prediction output page
└── README.md             # Project documentation
```

---

##  Requirements

- Python 3.7+
- pip (Python package installer)

---

## 🔧 Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/yourusername/fake-job-detector.git
cd fake-job-detector
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Train the Model (Optional)

> Note: A pre-trained model `job_model.pkl` is already included. You can retrain if needed.

```
python model_train.py
```

---

##  Running the App

Start the Flask development server:

```
python app.py
```

Then open your browser and visit:

```
http://localhost:5000
```

---

## ⚙ How It Works

1. User fills out job posting form (title, description, etc.)
2. Input is vectorized and passed to the pre-trained model
3. Model returns a binary prediction:
   -  **Legit Job Posting**
   -  **Fake Job Posting**

---

##  Model Info

- **Algorithm**: Random Forest Classifier
- **Trained On**: Job listings dataset with real and fake labels
- **Feature Engineering**: Basic NLP and label encoding (example: 'has_logo' as 0/1)

---

##  How to Use

### Step 1: Upload Job Info
Fill in the job title, description, etc.
<img width="1919" height="1079" alt="Screenshot 2025-08-01 101254" src="https://github.com/user-attachments/assets/31f0043d-7f40-4dae-883f-5435677c5e3f" />


### Step 2: Click Predict
The model will process the form and give a result.
<img width="1343" height="956" alt="Screenshot 2025-08-01 101512" src="https://github.com/user-attachments/assets/26d6d24f-68ef-495d-984c-83d576d99346" />


### Step 3: View Result
You'll see either ✅ Legit or ❌ Fake.
<img width="1454" height="947" alt="Screenshot 2025-08-01 101457" src="https://github.com/user-attachments/assets/2b0f2392-c7d0-4837-b011-4c4ac2d2df5b" />


---

##  Future Enhancements

- Use advanced NLP (TF-IDF, word embeddings)
- Add live data scraping and evaluation
- Deploy to cloud (Render, Heroku, AWS, etc.)
- Add user login/authentication
- Display prediction confidence scores

---


