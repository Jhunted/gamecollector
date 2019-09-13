from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Game, Location, Photo
from .forms import SessionForm

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'gamecollector1'

class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['name', 'genre', 'description', 'rating']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form) 

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['genre', 'description', 'rating']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  locations_game_doesnt_have = Location.objects.exclude(id__in = game.locations.all().values_list('id'))
  session_form = SessionForm()
  return render(request, 'games/detail.html', {
    'game': game,
    'session_form': session_form,
    'locations': locations_game_doesnt_have
  })

@login_required
def add_session(request, game_id):
  form = SessionForm(request.POST)
  if form.is_valid():
    new_session = form.save(commit=False)
    new_session.game_id = game_id
    new_session.save()
  return redirect('detail', game_id=game_id)

class LocationList(LoginRequiredMixin, ListView):
  model = Location

class LocationDetail(LoginRequiredMixin, DetailView):
  model = Location

class LocationCreate(LoginRequiredMixin, CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(LoginRequiredMixin, UpdateView):
  model = Location
  fields = ['name']

class LocationDelete(LoginRequiredMixin, DeleteView):
  model = Location
  success_url = '/locations/'

@login_required
def assoc_location(request, game_id, location_id):
  game = Game.objects.get(id=game_id)
  game.locations.add(location_id)
  return redirect('detail', game_id=game_id)

@login_required
def add_photo(request, game_id):
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
