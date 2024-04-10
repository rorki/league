from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):  
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class Team(models.Model):
    name = models.CharField(max_length=200)
    coach = models.ForeignKey(User, on_delete = models.DO_NOTHING, null=True)
    
    def __str__(self):
        return self.name


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete = models.DO_NOTHING)
    player = models.ForeignKey(Player, on_delete = models.DO_NOTHING)
    
    def __str__(self):
        return f"Team = {self.team}, player = {self.player}"