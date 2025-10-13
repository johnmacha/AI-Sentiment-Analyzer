from django.shortcuts import render
from transformers import pipeline
from django.http import JsonResponse

# Create your views here.
def home(request): #For GET
    return render(request, 'home.html')

def analyse_review(request): #For POST
    if request.method == 'POST':
        user_text = request.POST.get('review')

     #Load model once (expensive operation)/ Updated - Load only when needed
        sentiment_analyzer = pipeline(
        'sentiment-analysis',
        model="distilbert-base-uncased-finetuned-sst-2-english"
         )
        
        result = sentiment_analyzer(user_text)[0]

        label_map = {
            "NEGATIVE": "Negative 😡",
            # "NEUTRAL": "Neutral 🤔",
            "POSITIVE": "Positive 😊",
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



