from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class Board(models.Model):
    name = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return f"{self.name}"
