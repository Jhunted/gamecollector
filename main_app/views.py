from django.shortcuts import render

from django.http import HttpResponse

class Game:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, genre, description, rating):
    self.name = name
    self.genre = genre
    self.description = description
    self.rating = rating

cats = [
  Cat('Apex Legends', 'shooter', 'battle-royale', 5),
  Cat('Halo 3', 'shooter', 'first-person shooter', 5),
  Cat('Call of Duty', 'shooter', 'first-person shooter', 2)
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {'games': games})

