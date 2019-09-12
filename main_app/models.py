from django.db import models
from django.urls import reverse
from datetime import date

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

class Location(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('locations_detail', kwargs={'pk': self.id})

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

    def fed_for_today(self):
        return self.session_set.filter(date=date.today()).count() >= len(PLAYDAYS)

class Session(models.Model):
  date = models.DateField('session date')
  session = models.CharField(
    max_length=1,
    choices=PLAYDAYS,
    default=PLAYDAYS[0][0]
  )
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return "{self.get_playday_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  cat = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for game_id: {self.game_id} @{self.url}"