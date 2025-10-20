import gradio as gr
from transformers import pipeline

# Load model
sentiment_analyzer = pipeline(
    "sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Emoji mapping
label_map = {
    "POSITIVE": "😊 Positive",
    "NEGATIVE": "😡 Negative",
    "NEUTRAL": "🤔 Neutral",
}

# Define analysis function
def analyse_sentiment(text):
    result = sentiment_analyzer(text)[0]
    label = result['label'].upper()
    score = round(result['score'] * 100, 2)
    emoji = label_map.get(label, "❓ Unknown")
    return f"{emoji} ({score}%)"

# Gradio interface
iface = gr.Interface(
    fn=analyse_sentiment,
    inputs=gr.Textbox(lines=3, placeholder="Type your review here..."),
    outputs="text",
    title="AI Sentiment Analyzer 😊",
    description="Enter any text to get the sentiment!"
)

if __name__ == "__main__":
    iface.launch()
