import uuid
from django.db import models
from django.conf import settings
import random

class Game(models.Model):
    game_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    players = models.ManyToManyField('Hand', related_name="board")
    scores = models.ManyToManyField('Score', related_name="board")
    is_public = models.BooleanField(default=True)
    join_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    active = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)


class Hand(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    d1 = models.IntegerField(default=random.randint(1,6))
    d2 = models.IntegerField(default=random.randint(1,6))
    d3 = models.IntegerField(default=random.randint(1,6))
    d4 = models.IntegerField(default=random.randint(1,6))
    d5 = models.IntegerField(default=random.randint(1,6))
    roll_count = models.IntegerField(default=2)
    rem_rounds = models.IntegerField(default=13)
    yahtzee_flag = models.IntegerField(null=True)

    #Provides initial roll, decrements the remaining rounds and resets the roll count
    def init(self):
        self.d1 = random.randint(1,6)
        self.d2 = random.randint(1,6)
        self.d3 = random.randint(1,6)
        self.d4 = random.randint(1,6)
        self.d5 = random.randint(1,6)
        self.rem_rounds -= 1
        self.roll_count = 2
        self.save()

    # Method to pass in dice values from controller, and either generate new random numbers,
    # or keep passed in number to save to hand.
    @classmethod
    def rolldice (self, dice):
      if dice == 0:
        return random.randint(1,6)
      elif dice > 0:
        return dice

    def reduceRC(self):
        if self.roll_count > 0:
          self.roll_count -= 1
          self.save()
          return 0
        else:
          return 1
    #Yahtzee has two sections, an upper section and a lower section.
    #Upper section only counts dice that match the descriptor or returns zero

    def sumOnes (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        if x == 1:
          sum += 1
      return sum

    def sumTwos (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        if x == 2:
          sum += 2
      return sum

    def sumThrees (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        if x == 3:
          sum += 3
      return sum

    def sumFours (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        if x == 4:
          sum += 4
      return sum

    def sumFives (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        if x == 5:
          sum += 5
      return sum

    def sumSixes (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        if x == 6:
          sum += 6
      return sum
    #Chance = sum of dice and is a catch-all for Yahtzee
    #Creates an array of the 5 dice values, then returns sum of dice
    def chance(self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      sum = 0
      for x in dice:
        sum += x
      return sum
    #If there are three of a kind, the score returned is the total of all 5 dice, else 0
    #Creates a sorted array of the 5 dice values, then returns sum of 5 dice if three of a kind or zero.
    def threeOAK(self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      dice.sort()
      if (dice[0] == dice[1] and dice[1] == dice[2]):
        return self.chance()
      elif (dice[1] == dice[2] and dice[2] == dice[3]):
        return self.chance()
      elif (dice[2] == dice[3] and dice[3] == dice[4]):
        return self.chance()
      #For the Joker Rules, we need to check if the yahtzee field has already been filled
      elif (self.yahtzee_flag is not None and self.yahtzee == 50):
        return self.chance()
      else:
        return 0
    #Four of a kind is the same
    #Creates a sorted array of the 5 dice values, then returns sum of 5 dice if four of a kind or zero.
    def fourOAK (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      dice.sort()
      if (dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3]):
        return self.chance()
      elif (dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]):
        return self.chance()
      #For the Joker Rules, we need to check if the yahtzee field has already been filled
      elif (self.yahtzee_flag is not None and self.yahtzee == 50):
        return self.chance()
      else:
        return 0
    #Full house returns 25 or 0
    #Creates a sorted array of the 5 dice values, then returns 25 if a full house or zero.
    #After some deliberation and internet searching, we decided that a Yahtzee is not a full house.
    #This only matters if the Yahtzee box is filled in with 0 and a Yahtzee is scored, but hey... attention to detial.
    def fullHouse (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      dice.sort()
      if (dice[0] == dice[1] and dice[1] == dice[2] and dice[2] != dice[3] and dice[3] == dice[4]):
        return 25
      elif (dice[0] == dice[1] and dice[1] != dice[2] and dice[2] == dice[3] and dice[3] == dice[4]):
        return 25
      #For the Joker Rules, we need to check if the yahtzee field has already been filled
      elif (self.yahtzee_flag is not None and self.yahtzee == 50):
        return 25
      else:
        return 0
    #Small straight = 30
    #Creates a sorted array of the 5 dice values, then returns 30 if a small straight or zero.
    def smallStraight (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      values = []
      count = 0
      for x in dice:
          if x not in values:
            values.append(x)
            count += 1
      values.sort()
      if (count > 3):
          if (values[0]+1 == values[1] and values[1]+1 == values[2] and values[2]+1 == values[3]):
              return 30
          elif (values[1]+1 == values[2] and values[2]+1 == values[3] and values[3]+1 == values[4]):
              return 30
          #For the Joker Rules, we need to check if the yahtzee field has already been filled
          elif (self.yahtzee_flag is not None and self.yahtzee == 50):
              return 30
          else:
              return 0
      else:
        return 0
    #Large straight = 40
    #Creates a sorted array of the 5 dice values, then returns 40 if a large straight or zero.
    def largeStraight (self):
      dice = [self.d1,self.d2,self.d3,self.d4,self.d5]
      dice.sort()
      if (dice[0]+1 == dice[1] and dice[1]+1 == dice[2] and dice[2]+1 == dice[3] and dice[3]+1 == dice[4]):
        return 40
      #For the Joker Rules, we need to check if the yahtzee field has already been filled
      elif (self.yahtzee_flag is not None and self.yahtzee == 50):
        return 40
      else:
        return 0
    #Yahtzee (5 of a kind) = 50
    #Given an array of 5 dice values, returns 50 if a five of a kind or zero.
    def yahtzee (self):
      if (self.d1 == self.d2 and self.d2 == self.d3 and self.d3 == self.d4 and self.d4 == self.d5):
        return 50
      else:
        return 0

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
    chance = models.IntegerField(null=True)
    bonus_yahtzees = models.IntegerField(default=0)

    #Given an array of scores from model, return total score, WIP
    def sumValues(self):
        upper = 0
        if (self.ones is not None): upper +=self.ones
        if (self.twos is not None): upper +=self.twos
        if (self.threes is not None): upper +=self.threes
        if (self.fours is not None): upper +=self.fours
        if (self.fives is not None): upper +=self.fives
        if (self.sixes is not None): upper +=self.sixes
        upper_bonus = 0
        if (upper >= 63):
            upper_bonus = 35
        lower = 0
        if (self.three_oak is not None): lower +=self.three_oak
        if (self.four_oak is not None): lower +=self.four_oak
        if (self.full_house is not None): lower +=self.full_house
        if (self.small_straight is not None): lower +=self.small_straight
        if (self.large_straight is not None): lower +=self.large_straight
        if (self.yahtzee is not None): lower +=self.yahtzee
        if (self.chance is not None): lower +=self.chance
        return upper + upper_bonus + lower + ( self.bonus_yahtzees * 100 )
