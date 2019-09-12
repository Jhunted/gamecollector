#routers
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_session/', views.add_session, name='add_session'),
    path('games/<int:game_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
    path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
]