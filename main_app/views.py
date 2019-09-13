from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Game, Location, Photo
from .forms import SessionForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-jbc'

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'genre', 'description', 'rating']

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'rating']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  locations_game_doesnt_have = Location.objects.exclude(id__in = game.locations.all().values_list('id'))
  session_form = SessionForm()
  return render(request, 'games/detail.html', {
    'game': game,
    'session_form': session_form,
    'locations': locations_game_doesnt_have
  })

def add_session(request, game_id):
  form = SessionForm(request.POST)
  if form.is_valid():
    new_session = form.save(commit=False)
    new_session.game_id = game_id
    new_session.save()
  return redirect('detail', game_id=game_id)

class LocationList(ListView):
  model = Location

class LocationDetail(DetailView):
  model = Location

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(UpdateView):
  model = Location
  fields = ['name']

class LocationDelete(DeleteView):
  model = Location
  success_url = '/locations/'

def assoc_location(request, game_id, location_id):
  game = Game.objects.get(id=game_id)
  game.locations.add(location_id)
  return redirect('detail', game_id=game_id)

def add_photo(request, cat_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        photo = Photo(url=url, game_id=game_id)
        photo.save()
    except:
        print('An error occurred uploading file to S3')
  return redirect('detail', game_id=game_id)
