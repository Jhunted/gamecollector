from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'