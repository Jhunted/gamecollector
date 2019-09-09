from django.shortcuts import render
from .models import Game

# from django.http import HttpResponse

# class Game:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, genre, description, rating):
#     self.name = name
#     self.genre = genre
#     self.description = description
#     self.rating = rating

# games = [
#   Game('Apex Legends', 'shooter', 'battle-royale', 5),
#   Game('Halo 3', 'shooter', 'first-person shooter', 5),
#   Game('Call of Duty', 'shooter', 'first-person shooter', 2)
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game': game})
