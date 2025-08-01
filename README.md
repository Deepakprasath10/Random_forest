# Random_forest
# Fake Job Posting Detector

A simple machine learning-based web application that predicts whether a job posting is **legit or fake**, using a **Random Forest Classifier**, built with **Flask**.

---

##  Features

- Detects fake job listings using input features like title, description, logo, and more
- Intuitive and responsive user interface
- Built using Python and Flask
- Trained using a Random Forest Classifier
- Model trained on job postings dataset with labeled fake and real jobs

---

##  Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fake-job-detector.git
cd fake-job-detector
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Train the Model (Optional)
A pre-trained model (job_model.pkl) is already included. If you want to retrain the model:

bash
Copy
Edit
python model_train.py
🚦 Running the Application
Start the Flask development server:

bash
Copy
Edit
python app.py
Then open your browser and go to:

arduino
Copy
Edit
http://localhost:5000
⚙️ How It Works
The app uses a Random Forest Classifier trained on a dataset of job listings.

When a user fills in the job details like title, description, location, etc.:

The model processes the input and makes a binary classification.

The prediction is shown as:
✅ Legit Job Posting or ❌ Fake Job Posting

📁 File Structure
php
Copy
Edit
fake-job-detector/
├── app.py                # Flask application
├── model_train.py        # ML model training script
├── job_model.pkl         # Pre-trained RandomForest model
├── static/
│   └── style.css         # Custom styles for the web app
├── templates/
│   ├── index.html        # Form input page
│   └── result.html       # Prediction output page
├── requirements.txt      # Python dependencies
└── README.md             # This documentation
 Future Improvements
Integrate NLP techniques for deeper text analysis

Add more metadata fields for better accuracy

Deploy online using platforms like Heroku, Render, or AWS

Add input validations and pre-processing feedback

📸 Step-by-Step Guide: How to Use the Fake Job Detector
Step 1: Input Form
Fill out the form fields like job title, description, logo flag, etc.

Step 2: Submit
Click the Predict button to get the result.

Step 3: Prediction Result

See whether the job is legit ✅ or fake ❌.
