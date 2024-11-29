# backend/game/urls.py
from django.urls import path
from .views import ScoreListCreateView, UserScoreListView

urlpatterns = [
    path('submit-score/', ScoreListCreateView.as_view(), name='submit_score'),
    path('user-scores/', UserScoreListView.as_view(), name='user_scores'),
    
]