# Sentiment Analysis Flask App

## 🚀 Overview

This project is a Flask-based web application that performs sentiment analysis using a trained NLP model. The app takes user input text, processes it using TF-IDF vectorization, and predicts whether the sentiment is positive, negative or neutral.

## 📦 Features

- **Text Input:** Accepts text input from users.
- **Model Prediction:** Uses a pre-trained machine learning model for sentiment classification.
- **User Interface:** A simple UI to interact and get sentiment results using Flask.

## 🔧 Installation

Follow these steps to run the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AdityaBhoir510/NLP_sentimental_analysis.git
   cd sentiment-analysis-flask
   ```

2. **Create and activate a virtual environment:**

   ```bash
   # For Windows
   python -m venv venv
   .\venv\Scripts\activate

   # For Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

5. **Access the app:** Open your browser and go to:

   ```
   http://localhost:5000
   ```


## 📸 Screenshots

Add screenshots here to showcase your app's interface or Postman tests.

## 📚 Project Structure

```
.
├── app.py
├── requirements.txt
├── model.pkl
├── tfidf_vectorizer.pkl
├── Sementic_analysis_X_dataset.ipynb
├── README.md
├── static/css
├── static/img
└── templates/
```

## 🧠 How It Works

1. **Text Processing:** Uses TF-IDF vectorization to convert text into numerical features.
2. **Model Prediction:** The trained model classifies the sentiment.
3. **Predication Results:** Displays Prediction Results as 'Positive', 'Negative' or 'Neutral' on browser.

## ✨ Future Enhancements

- Integrate more advanced NLP models.
- Deploy the app to cloud platforms.
- Can be used as a API.

## 🛠️ Author

Aditya Bhoir — [LinkedIn Profile](www.linkedin.com/in/adityabhoir510) — [Portfolio](https://adityabdev.vercel.app/)

Feel free to reach out !

---

Star ⭐ this repo if you like the project!

