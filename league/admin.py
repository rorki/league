from django.contrib import admin

from .models import GamePlayer, Game

admin.site.register(Game)
admin.site.register(GamePlayer)
