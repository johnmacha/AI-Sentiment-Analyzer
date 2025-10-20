#About
- An AI-powered sentiment analysis web app built with Django and Hugging Face Transformers.
- This project analyzes user-input text and classifies it as Positive 😊, Neutral 🤔, or Negative 😡 using a pre-trained model.

#Features
- User input text analysis through a clean web interface
- Hugging Face sentiment model integration (distilbert-base-uncased-finetuned-sst-2-english or cardiffnlp/twitter-roberta-base-sentiment)
- Emoji-based sentiment visualization
- Real-time inference without needing to retrain models

- Modular Django structure for easy scalability

#Tech Stack
- Backend: Django (Python)
- AI / NLP: Hugging Face Transformers, PyTorch
- Frontend: HTML, CSS (Bootstrap)
- Version Control: Git & GitHub
- Deployment (optional): Heroku / Render / AWS

#How It Works
- User enters a review or comment.
- The app sends the text to a Hugging Face model using the transformers pipeline.
- The model predicts the sentiment label (Positive, Neutral, Negative).
- An appropriate emoji and confidence score are displayed.

#Requirements
- Python 3.8+
- Django 4.x
- Transformers
- Torch
- Requests

#Live Demo
- To have a peek on the live app visit https://huggingface.co/spaces/Juaan2/AI-Sentiment-Analyzer](https://huggingface.co/spaces/Juaan2/AI-Sentiment-Analyzer
