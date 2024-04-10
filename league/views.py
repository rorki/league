from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Game, Round
from team.models import Team
from django.db.models import Sum, When, Case, When

def index(request):
    return league(request, 16)
    
def league(request, round: int):
    round = Round(round)
        
    games_rs = Game.objects.annotate(score1 = Sum(Case(When(team1="gameplayer__team", then="gameplayer__score")), default = 0), 
                                     score2 = Sum("gameplayer__score", default = 0)).filter(round=round)
    games = []
    for game_rs in games_rs:
        game = {"team1": game_rs.team1.name,
                "team2": game_rs.team2.name,
                
                "score1": game_rs.score1,
                "score2": game_rs.score2,
                
                "round": game_rs.round,
                "date": game_rs.date
        }
        games.append(game)
    
    template = loader.get_template('league.html')
    context = {'games': games}
    return HttpResponse(template.render(context, request))
