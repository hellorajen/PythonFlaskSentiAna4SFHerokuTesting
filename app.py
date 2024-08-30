from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '')
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    result = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
    return jsonify({'sentiment': result})

if __name__ == '__main__':
    app.run(debug=True)
