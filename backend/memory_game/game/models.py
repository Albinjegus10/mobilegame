from django.db import models

from django.db import models
from django.conf import settings

from django.conf import settings

# game/models.py
from django.db import models
from django.conf import settings

class Score(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='scores'
    )
    moves = models.IntegerField()
    time_taken = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_played']
        verbose_name_plural = 'Scores'

    def __str__(self):
        return f"{self.user.username} - {self.date_played}"

    
