from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return "Sentiment Analysis API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    
    # Transform text using TF-IDF vectorizer
    text_tfidf = vectorizer.transform([text])
    
    # Predict sentiment
    prediction = model.predict(text_tfidf)[0]
    sentiment = 'positive' if prediction == 1 else 'neutral' if prediction == 0 else 'negative'
    
    return jsonify({'text': text, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
