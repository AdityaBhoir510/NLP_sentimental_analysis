from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form['tweet']
        print(data)
        
        # Transform text using TF-IDF vectorizer
        text_tfidf = vectorizer.transform([data])
        
        # Predict sentiment
        prediction = model.predict(text_tfidf)[0]
        sentiment = 'Positive' if prediction == 1 else 'Neutral' if prediction == 0 else 'Negative'
        
        # return jsonify({'text': text, 'sentiment': sentiment})
        return render_template('index.html',result=sentiment, tweet=data)

if __name__ == '__main__':
    app.run(debug=True)
