from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyse/', views.analyse_review, name='analyse_review'),
]