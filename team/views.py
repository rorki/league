from django.http import HttpResponse
from django.template import loader
from .models import TeamPlayer, Team
from django.db.models import Sum, When, Case, When, Count, Avg

def index(request):
    if request.user.is_authenticated and request.user.groups.filter(name = "Coaches").exists():
        team_obj = Team.objects.get(coach=request.user.id)
        return team(request, team_obj.id)
    else:
        template = loader.get_template('forbidden.html')
        return HttpResponse(template.render({}, request))

def team(request, id: int):
    """
    Rer
    """
    template = loader.get_template('team.html')
    team = Team.objects.get(id=id)
    team_players_rs = TeamPlayer.objects.annotate(
                                        ngames = Count("team__gameplayer__game", distinct=True),
                                        avg_score = Avg("team__gameplayer__score", default = 0),
                                    ).filter(team=id)
    
    team_players = []
    for team_player_rs in team_players_rs:
        team_player = {
            "name": team_player_rs.player.name,
            "number_of_games": team_player_rs.ngames,
            "average_score": team_player_rs.avg_score
        }
        team_players.append(team_player)
    
    context = {
        'team': team.name,
        'players': team_players,
    }
    return HttpResponse(template.render(context, request))


def admin(request):
    """
    Retrieves stats for all teams participatng in the league.
    Can be only accessed by users from Admins group.
    """
    
    if not request.user.is_authenticated or not request.user.groups.filter(name = "Admins").exists():
        template = loader.get_template('forbidden.html')
        return HttpResponse(template.render({}, request))
        
    template = loader.get_template('admin.html')
    teams_rs = Team.objects.annotate(team1_games=Count('team1'), team2_games=Count('team2')).select_related("coach").order_by("name")
    teams = []
    
    for team_rs in teams_rs:
        team_info = {
            "id": team_rs.id,
            "name": team_rs.name,
            "coach": "" if not team_rs.coach else f"{team_rs.coach.first_name} {team_rs.coach.last_name}",
            "games": team_rs.team1_games + team_rs.team2_games
        }
        teams.append(team_info)
      
    context = {
        'teams': teams,
    }
    return HttpResponse(template.render(context, request))
