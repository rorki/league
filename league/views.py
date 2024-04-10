from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Game, Round, GamePlayer
from team.models import Team
from django.db.models import Sum, When, Case, When

def index(request):
    return league(request, 16)
    
def league(request, round: int):
    round = Round(round)
        
    games_rs = Game.objects.filter(round=round) 
    game_scores = GamePlayer.objects.values("team", "game").annotate(score = Sum("score"))
    game_score_map = {(gs["team"], gs["game"]): gs["score"] for gs in game_scores}
    games = []
    for game_rs in games_rs:
        game = {"team1": game_rs.team1.name,
                "team2": game_rs.team2.name,
                
                "score1": game_score_map.get((game_rs.team1.id, game_rs.id), 0),
                "score2": game_score_map.get((game_rs.team2.id, game_rs.id), 0),
                
                "round": game_rs.round,
                "date": game_rs.date
        }
        games.append(game)
    
    template = loader.get_template('league.html')
    context = {'games': games}
    return HttpResponse(template.render(context, request))
