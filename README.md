# AI-Based Sentiment Analyzer

This is a simple AI-based sentiment analyzer built using Python, Flask, and Hugging Face Transformers. It detects the sentiment of user-provided text (e.g., reviews or comments) and classifies it as **Positive** or **Negative**.

## 🔧 Technologies Used
- Python
- Flask
- Hugging Face Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)

## 🚀 Features
- Analyze input text and return sentiment
- Lightweight and runs locally
- No database required (MongoDB version optional)

## 💻 How to Run

1. Install dependencies:
```bash
pip install flask transformers torch
