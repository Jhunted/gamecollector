from django.contrib import admin
from .models import Game, Session, Location, Photo

# Register your models here.

admin.site.register(Game)
admin.site.register(Session)
admin.site.register(Location)
admin.site.register(Photo)
