from django.urls import path

from . import views


app_name = 'cricapp'

urlpatterns = [
    path(  # home
        '',
        views.home,
        name='home'
    ),
    path(  # Add team
        'team/add',
        views.add_team,
        name='add_team'
    ),
    path(  # List of teams
        'team/list',
        views.teams,
        name='teams'
    ),
    path(  # Team detail
        'team/<int:pk>/',
        views.team_detail,
        name='team_detail'
    ),
    path(  # Add player
        'player/add',
        views.add_player,
        name='add_player'
    ),
    path(  # Add player
        'player/add/<int:pk>/',
        views.add_player,
        name='add_team_player'
    ),
    path(  # List of players
        'player/list',
        views.players,
        name='players'
    ),
    path(   # Player details
        'player/<int:id>/',
        views.player_details,
        name='player_details'
    ),
    path(  # Matches
        'matches',
        views.matches,
        name='matches'
    ),
    path(
        'matches/fixtures',
        views.create_matches_fixtures,
        name='create_fixtures'
    ),
    path(
        'match/<int:pk>',
        views.match_details,
        name='match_details'
    ),
    path(
        'all_fixtures',
        views.fixture_list,
        name='all_fixture_list'
    ),
    path(
        'all_fixtures/<str:trnmt_id>/',
        views.fixture_list,
        name='single_fixture_list'
    ),
    path(
        'process/<int:team_id>/<int:match_id>/<str:trnmt_id>/',
        views.select_match_winner,
        name='select_match_winner'
    ),
    path(
        'semi_process/<int:team1_id>/<int:team2_id>/<str:trnmt_id>/',
        views.select_semifinalist,
        name='select_semifinalist'
    ),
    path(
        'final_process/<int:team1_id>/<int:team2_id>/<str:trnmt_id>/',
        views.select_finalist,
        name='select_finalist'
    )
]
