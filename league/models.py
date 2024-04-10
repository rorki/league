from django.db import models
from team.models import Team, Player

class Round(models.IntegerChoices):
    SIXTEENTH = 16, '16th-finals'
    EIGHTH = 8, 'Eighth-finals'
    QUARTER = 4, 'Quarterfinals'
    SEMIFINAL = 2, 'Semifinals'
    FINAL = 1, 'Final'

class Game(models.Model):
    team1 = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = "team1")
    team2 = models.ForeignKey(Team, on_delete = models.CASCADE, related_name = "team2")
    round = models.IntegerField(default=Round.SIXTEENTH, choices=Round.choices)
    
    date = models.DateTimeField()
    
    def __str__(self):
        return f"Team1 = {self.team1}, team2 = {self.team2}, round = {self.round}"
    

class GamePlayer(models.Model):
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    player = models.ForeignKey(Player, on_delete = models.CASCADE)
    
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Game = {self.game}, team = {self.team}, player = {self.player}"

    