import itertools
import random
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from .model_forms import TeamForm, PlayerForm
from .models import *
from django.contrib import messages


def home(request):
    """
    Display Point and match details on the home page.

    Parameters
    ----------
    request : HTTP request object

    Returns : Render the home page template.

    """
    matches = Match.objects.all().order_by('-match_number')
    teams = Team.objects.all()
    context = {
        'matches': matches,
        'teams': teams
    }
    return render(request, 'home.html', context)


def add_team(request):
    """
    Provide functionality to add team.

    Parameters
    ----------
    request : HTTP request object

    Returns : Render the add team page template.

    """
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team has been added successfully')
        return redirect('cricapp:teams')
    else:
        form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'teams/add.html', context)


def team_detail(request, pk=None):
    """
    List all the details of a particular Team.

    Parameters
    ----------
    request : HTTP request object
    pk: Primary key of the Team entity

    Returns : Render the add team page template.

    """
    if pk is not None:
        context = dict()
        context['team'] = Team.objects.get(pk=pk)
        context['players'] = Player.objects.filter(team=pk)
        return render(request, 'teams/details.html', context)
    else:
        return redirect('home')


def teams(request):
    """
    List all of the teams.

    Parameters
    ----------
    request : HTTP request object

    """

    context = {
        'teams_list': Team.objects.all(),
    }
    return render(request, 'teams/list.html', context)


def add_player(request, pk=None):
    """
    Provide functionality to add player.

    Parameters
    ----------
    request : HTTP request object

    Returns : Render the add player template.

    """
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player has been added successfully')
        return redirect('cricapp:players')
    else:
        team = pk if id is not None else ''
        form = PlayerForm(initial={'team': team})

    context = {'form': form}
    return render(request, 'players/add.html', context)


def players(request):
    """
    List players.

    Parameters
    ----------
    request : HTTP request object.
    Returns : Render the list player template.

    """

    players = Player.objects.all()
    context = {'players_list': players}
    return render(request, 'players/list.html', context)


def player_details(request, id):
    """
    List details of a particular player.

    Parameters
    ----------
    request : HTTP request object.
    Returns : Render the add player detail template.

    """

    player = get_object_or_404(Player, pk=id)
    team = Team.objects.filter(
        pk=player.team_id)[0].name
    context = {
        'player': player,
        'team': team
    }

    return render(request, 'players/detail.html', context)


def matches(request):
    """
    List Matches.

    Parameters
    ----------
    request : HTTP request object
    Returns : Render the match listing template.

    """
    context = {'match_list': Match.objects.all()}
    return render(request, 'matches/list.html', context)


def create_matches_fixtures(request):
    """
    Dynamically create match fixrures.

    Parameters
    ----------
    request : HTTP request object.

    Returns : Render the create tournament template.

    """
    Match.objects.all().delete()
    Team.objects.all().update(**{'points': 0})
    all_teams = Team.objects.all()

    match_possibilities = itertools.combinations(all_teams, 2)

    all_matches = list()
    tournament_no = str(random.randint(1, 999999999999999))
    i = 1
    for combination in match_possibilities:
        all_matches.append(combination)
        Match(**{'team1': combination[0], 'team2': combination[1], 'level': 'Round1', 'tournament_id': tournament_no, 'location': f'location_{i}', 'stadium': f'stadium_{i}',
                 'match_number': f'match_{i}'}).save()
        i = i+1

    return render(request, 'matches/create_tournament.html',
                  {'tournament_no': tournament_no, 'match_possibilities': all_matches})


def match_details(request, pk):
    """
    Display match details.

    Parameters
    ----------
    request : HTTP request object
    pk: primary key of entity Match.

    -------------------
    Returns : Render the match detail template.

    """
    match = get_object_or_404(Match, pk=pk)
    context = {'match': match}
    return render(request, 'matches/detail.html', context)


def fixture_list(request, trnmt_id=None):
    """
    Match fixtures.

    Parameters
    ----------
    request : HTTP request object.
    trnmt_id: Tournament id.

    -------------------
    Returns : Render the match fixture template.


    """
    context = dict()
    if trnmt_id is None:
        trnmt_id = Match.objects.all()[0].tournament_id

    # tournament id
    context['trmt_id'] = trnmt_id
    # teams
    context['teams'] = Team.objects.values(
        'name', 'points').all().order_by('-points')
    # Get fixture list
    all_fixtures = Match.objects.filter(tournament_id=trnmt_id)

    if Match.objects.filter(tournament_id=trnmt_id, team_winner__isnull=False).count() == all_fixtures.count():
        # Qualified teams
        context['qualified_teams'] = [{'name': team.name, 'id': team.id, 'is_win': Match.objects.filter(team_winner=team, level='Semi').count()}
                                      for team in Team.objects.all().order_by('-points')[0:4]]

    # Teams who will participate in final and winner.
    if Match.objects.filter(level='Semi', tournament_id=trnmt_id, team_winner__isnull=False).count() == 2:
        context['final_teams'] = [{'name': match.team_winner.name, 'id': match.team_winner.id}
                                  for match in Match.objects.filter(level='Semi', tournament_id=trnmt_id)]
        context['final_winner'] = Match.objects.filter(level='Final')[
            0].team_winner.name if Match.objects.filter(level='Final').count() > 0 else False
    # matches
    matches = list()
    for fix in all_fixtures:
        is_done = 'Yes' if fix.team_winner is not None else 'No'
        matches.append({'team1': fix.team1, 'team2': fix.team2, 'location': fix.location, 'stadium': fix.stadium, 'trmt_id': fix.tournament_id,
                        'team1_id': fix.team1.id, 'team2_id': fix.team2.id, 'match_id': fix.id, 'match_win': fix.team_winner, 'is_completed': is_done})

    context['matches'] = matches

    return render(request, 'matches/fixtures.html', context)


def select_match_winner(request, team_id=None, match_id=None, trnmt_id=None):
    """
    Functionality to select match winner.

    Parameters
    ----------
    request : HTTP request object
    team_id: Winner Team id.
    match_id: Match id.
    trnmt_id: Tournament id.

    ----------------------------
    return: redirects to fixture listing page.


    """
    if team_id is not None and match_id is not None and trnmt_id is not None:
        point = Team.objects.get(pk=team_id).points
        Match.objects.filter(pk=match_id).update(**{'team_winner': team_id})
        Team.objects.filter(pk=team_id).update(**{'points': int(point)+2})
        return redirect('cricapp:single_fixture_list', trnmt_id)
    else:
        return redirect('cricapp:all_fixture_list')


def select_semifinalist(request, team1_id=None, team2_id=None, trnmt_id=None):
    """
    Functionality to select semi finalist.

    Parameters
    ----------
    request : HTTP request object
    team1_id: Team one id.
    team2_id: Team two id.
    trnmt_id: Tournament id.

    ----------------------------
    return: redirects to fixture listing page.

    """
    if team1_id is not None and team2_id is not None and trnmt_id is not None:
        match_number = Match.objects.filter(tournament_id=trnmt_id).count() + 1
        Match(**{'team1_id': team1_id, 'team2_id': team2_id, 'level': 'Semi', 'tournament_id': trnmt_id,
                 'match_number': match_number, 'team_winner_id': team1_id}).save()
        return redirect('cricapp:single_fixture_list', trnmt_id)
    else:
        return redirect('cricapp:all_fixture_list')


def select_finalist(request, team1_id=None, team2_id=None, trnmt_id=None):
    """
    Functionality to select finalist.

    Parameters
    ----------
    request : HTTP request object
    team1_id: Team one id.
    team2_id: Team two id.
    trnmt_id: Tournament id.

    ----------------------------
    return: redirects to fixture listing page.

    """
    if team1_id is not None and team2_id is not None and trnmt_id is not None:
        match_number = Match.objects.filter(tournament_id=trnmt_id).count() + 1
        Match(**{'team1_id': team1_id, 'team2_id': team2_id, 'level': 'Final', 'tournament_id': trnmt_id,
                 'match_number': match_number, 'team_winner_id': team1_id}).save()
        return redirect('cricapp:single_fixture_list', trnmt_id)
    else:
        return redirect('cricapp:all_fixture_list')
