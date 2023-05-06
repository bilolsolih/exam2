from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from .choices import PLAYER_POSITION, REFEREE_POSITION, GOAL_TYPE, CARD_TYPE, CARD_REASONS


class Country(models.Model):
    title = models.CharField(max_length=128)
    flag = models.ImageField(upload_to='football/countries/flags/')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class League(models.Model):
    country = models.ForeignKey(Country, related_name='leagues', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'


class Match(models.Model):
    host = models.ForeignKey('football.Team', related_name='matches_as_host', on_delete=models.SET_NULL, null=True)
    guest = models.ForeignKey('football.Team', related_name='matches_as_guest', on_delete=models.SET_NULL, null=True)
    host_goals = models.PositiveIntegerField(default=0)
    guest_goals = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    match_order_number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(2)])
    is_finished = models.BooleanField(default=True)
    referee = None

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    @property
    def result(self):
        if self.host_goals > self.guest_goals:
            return f'Winner is {self.host.title}'
        elif self.host_goals < self.guest_goals:
            return f'Winner is {self.guest.title}'
        else:
            return 'Draw'

    def __str__(self):
        return f'Match between {self.host} and {self.guest}'


class Referee(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    position = models.CharField(choices=REFEREE_POSITION, max_length=2)

    class Meta:
        verbose_name = 'Referee'
        verbose_name_plural = 'Referees'


class Team(models.Model):
    title = models.CharField(max_length=128)
    flag = models.ImageField(upload_to='football/teams/flags/')
    league = models.ForeignKey(to='football.League', related_name='teams', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Player(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    player_number = models.PositiveIntegerField(default=0)
    position = models.CharField(choices=PLAYER_POSITION, max_length=2)
    team = models.ForeignKey(to='football.League', related_name='players', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'


class Goal(models.Model):
    match = models.ForeignKey(to='football.Match', related_name='goals', on_delete=models.CASCADE)
    player = models.ForeignKey(to='football.Player', related_name='goals', on_delete=models.CASCADE)
    type = models.CharField(choices=GOAL_TYPE, max_length=2, default='nm')
    scored_minute = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'


class Card(models.Model):
    type = models.CharField(choices=CARD_TYPE, max_length=1)
    referee = models.ForeignKey(to='football.Referee', related_name='cards', on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey(to='football.Match', related_name='cards', on_delete=models.CASCADE)
    player = models.ForeignKey(to='football.Player', related_name='cards', on_delete=models.CASCADE)
    reason = models.CharField(choices=CARD_REASONS, max_length=2)
    given_minute = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
