from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=255)
    logo_uri = models.CharField(max_length=2048)
    club_state = models.CharField(max_length=255)
    points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.name


class Player(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_uri = models.CharField(max_length=2048)
    jersey_number = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Players"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Match(models.Model):

    team1 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team2')
    match_number = models.CharField(max_length=128)
    level = models.CharField(max_length=100, blank=True, null=True)
    tournament_id = models.CharField(max_length=255)
    team_winner = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team_winner', blank=True, null=True)
    location = models.CharField(max_length=128)
    stadium = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name_plural = "Matches"
