
from rest_framework import serializers
from .models import Score
from django.contrib.auth import get_user_model
from django.conf import settings


class ScoreSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), write_only=True)
    class Meta:
        model = Score
        fields = ['user','moves','time_taken']
        read_only_fields = ['date_played']