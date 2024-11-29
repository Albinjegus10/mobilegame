from django.shortcuts import render

# Create your views here.
# backend/game/views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Score
from .serializers import ScoreSerializer
from rest_framework import generics
from .models import Score
from .serializers import ScoreSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Score
from .serializers import ScoreSerializer

class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [AllowAny]  # Allows all users to submit scores

    def perform_create(self, serializer):
        # If a user is authenticated, use their user instance
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            # Optionally, you might want to handle anonymous score submission differently
            # For now, we'll allow it but you may want to add custom logic
            serializer.save()
            

class UserScoreListView(generics.ListAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Get top 10 scores sorted by moves (lower is better)
        top_scores = Score.objects.order_by('moves', 'time_taken')[:10]
        serializer = ScoreSerializer(top_scores, many=True)
        return Response(serializer.data)

