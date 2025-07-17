from flask import Flask, request, jsonify
from transformers import pipeline
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Load Hugging Face sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Connect to MongoDB (local)
client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_db"]
collection = db["results"]

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_pipeline(text)[0]
    
    # Save result to MongoDB
    record = {
        "text": text,
        "label": result['label'],
        "score": round(result['score'], 2),
        "timestamp": datetime.now()
    }
    collection.insert_one(record)

    return jsonify(record)

@app.route("/history", methods=["GET"])
def history():
    results = list(collection.find({}, {"_id": 0}).sort("timestamp", -1))
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
