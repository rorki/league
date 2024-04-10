from django.contrib import admin

from .models import Team, TeamPlayer, Player


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(TeamPlayer)
