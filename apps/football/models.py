from django.db import models
from django.utils import timezone


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


class Team(models.Model):
    title = models.CharField(max_length=128)
    player = None
