from django.shortcuts import render, redirect
from transformers import pipeline
from django.http import JsonResponse

#Load model once (expensive operation)
sentiment_analyzer = pipeline(
    'sentiment-analysis',
    model="cardiffnlp/twitter-roberta-base-sentiment"
    )

# Create your views here.
def home(request): #For GET
    return render(request, 'home.html')

def analyse_review(request): #For POST
    if request.method == 'POST':
        user_text = request.POST.get('review')
        result = sentiment_analyzer(user_text)[0]

        label_map = {
            "LABEL_0": "Negative 😡",
            "LABEL_1": "Neutral 🤔",
            "LABEL_2": "Positive 😊",
        }
        
        sentiment_text = label_map.get(result['label'], "Unknown ❓")
        score = round(result['score'] * 100, 2)

        context = {
            'review': user_text,
            'sentiment': sentiment_text,
            'score': score,
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')



