import uuid
from django.db import models
from django.conf import settings

class Game(models.Model):
    game_id = models.UUIDField(default=uuid.uuid4, editable=False, max_length=10)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    is_public = models.BooleanField()
    join_code = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)

class Hand(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    d1 = models.IntegerField()
    d2 = models.IntegerField()
    d3 = models.IntegerField()
    d4 = models.IntegerField()
    d5 = models.IntegerField()
    
    def init(self):
        d1 = Ceil(Rand() * 6)
        d2 = Ceil(Rand() * 6)
        d3 = Ceil(Rand() * 6)
        d4 = Ceil(Rand() * 6)
        d5 = Ceil(Rand() * 6)
    
class Score(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    ones = models.IntegerField(null=True)
    twos = models.IntegerField(null=True)
    threes = models.IntegerField(null=True)
    fours = models.IntegerField(null=True)
    fives = models.IntegerField(null=True)
    sixes = models.IntegerField(null=True)
    three_oak = models.IntegerField(null=True)
    four_oak = models.IntegerField(null=True)
    full_house = models.IntegerField(null=True)
    small_straight = models.IntegerField(null=True)
    large_straight = models.IntegerField(null=True)
    yahtzee = models.IntegerField(null=True)
    yahtzee_Flag = models.BooleanField(default=False)
    bonus_Yahtzees = models.IntegerField(default=0)
    upper_bonus = models.IntegerField(default=0)
    
