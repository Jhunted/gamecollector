from django.db import models
from django.urls import reverse

# Create your models here.
PLAYDAYS = (
  ('S', 'Sunday'),
  ('M', 'Monday'),
  ('T', 'Tuesday'),
  ('W', 'Wednesday'),
  ('TR', 'Thursday'),
  ('F', 'Friday'),
  ('SAT', 'Saturday'),
)

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.id})

class Session(models.Model):
  date = models.DateField('session date')
  session = models.CharField(
    max_length=1,
    choices=PLAYDAYS,
    default=PLAYDAYS[0][0]
  )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return "{self.get_session_display()} on {self.date}"

  class Meta:
    ordering = ['-date']