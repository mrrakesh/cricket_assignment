import uuid

from django.test import TestCase
from django.urls import reverse

from .models import *


def _create_team(name, logo_uri='logo_uri', club_state='club_state', points=0):
    team = Team(name=name, logo_uri=logo_uri,
                club_state=club_state, points=points)
    team.save()
    return team


def _create_player(first_name="james",
                   last_name="vince", image_uri="http://example.com",
                   jersey_number=100, country="Earth", team_id=1):
    player = Player(first_name=first_name,
                    last_name=last_name, image_uri=image_uri,
                    jersey_number=jersey_number, country=country)
    return player


def _create_match(match_number=1, level='Test',
                  tournament_id="23121212"):
    match = Match(match_number=match_number, level=level,
                  tournament_id=tournament_id)
    return match


class TeamModelTest(TestCase):
    def test_team_create(self):
        name = "Greatest team ever"
        logo_uri = "http://foo.bar"
        club_state = "Earth"
        team = _create_team(name, logo_uri=logo_uri,
                            club_state=club_state)
        self.assertEqual(name, team.name)
        self.assertEqual(logo_uri, team.logo_uri)
        self.assertEqual(club_state, team.club_state)


class PlayerModelTest(TestCase):
    def test_player_create(self):
        first_name = "vince"
        last_name = "james"
        image_uri = "http://example.org"
        jersey_number = 10
        country = "Local"
        name = "Greatest team ever"
        logo_uri = "http://foo.bar"
        club_state = "Earth"
        team = _create_team(name, logo_uri=logo_uri,
                            club_state=club_state, points=0)
        player = _create_player(first_name=first_name,
                                last_name=last_name, image_uri=image_uri,
                                jersey_number=jersey_number, country=country)
        player.team = team
        player.save()

        self.assertEqual(first_name, player.first_name)
        self.assertEqual(last_name, player.last_name)
        self.assertEqual(image_uri, player.image_uri)
        self.assertEqual(jersey_number, player.jersey_number)
        self.assertEqual(country, player.country)
        self.assertEqual(team, team)


class MatchModelTest(TestCase):
    def test_match_create(self):
        match_number = 1
        tournament_id = "23121212"
        level = 'Test'
        name = "Greatest team ever"
        logo_uri = "http://foo.bar"
        club_state = "Earth"
        team = _create_team(name, logo_uri=logo_uri,
                            club_state=club_state, points=0)
        match = _create_match(match_number=match_number, level=level,
                              tournament_id=tournament_id)
        location = 'test'
        stadium = 'test'
        match.team1 = team
        match.team2 = team
        match.team_winner = team

        self.assertEqual(match_number, match.match_number)
        self.assertEqual(level, match.level)
        self.assertEqual(tournament_id, match.tournament_id)
