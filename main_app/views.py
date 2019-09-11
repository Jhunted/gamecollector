from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import SessionForm




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    session_form = SessionForm()
    return render(request, 'games/detail.html',
    { 'game': game, 'session_form': session_form })

class GameCreate(CreateView):
  model = Game
  fields = '__all__'

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'rating']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def add_session(request, game_id):
  form = SessionForm(request.POST)
  if form.is_valid():
    new_session = form.save(commit=False)
    new_session.game_id = game_id
    new_session.save()
  return redirect('detail', game_id=game_id)

