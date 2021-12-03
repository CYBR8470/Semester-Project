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
    #connect to game
    #connect to player
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
    yahtzee_Flag = models.Boolean(default=False)
    bonus_Yahtzees = models.IntegerField(default=0)
    upper_bonus = models.IntegerField(default=0)
    
