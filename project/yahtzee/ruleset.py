
#Yahtzee has two sections, an upper section and a lower section.

#Upper section only counts dice that match the descriptor or returns zero

#Given an array of dice values and a desired pip value, returns sum of all die with desired pip value
def sumVals (dice, val):
  sum = 0
  for x in dice:
    if x == val:
      sum += val
  return sum

#Lower section has more complex rules

#Chance = sum of dice and is a catch-all for Yahtzee
#Given an array of dice values, returns sum of dice
def chance (dice):
  sum = 0
  for x in dice:
    sum += x
  return sum

#Need to define joker bonus rules here
yahtzeeFlag = False
yahtzeeBonus = 0;

#If there are three of a kind, the score returned is the total of all 5 dice, else 0
#Given a sorted array of 5 dice values, returns sum of 5 dice if three of a kind or zero.
def threeOAK (dice):
  if (dice[0] == dice[1] and dice[1] == dice[2]):
    return chance(dice)
  elif (dice[1] == dice[2] and dice[2] == dice[3]):
    return chance(dice)
  elif (dice[2] == dice[3] and dice[3] == dice[4]):
    return chance(dice)
  else:
    return 0
#Four of a kind is the same
#Given a sorted array of 5 dice values, returns sum of 5 dice if four of a kind or zero.
def fourOAK (dice):
  if (dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3]):
    return chance(dice)
  elif (dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]):
    return chance(dice)
  else:
    return 0
#Full house returns 25 or 0
#Given a sorted array of 5 dice values, returns 25 if a full house or zero.
def fullHouse (dice):
  if (dice[0] == dice[1] and dice[1] == dice[2] and dice[3] == dice[4]):
    return 25
  elif (dice[0] == dice[1] and dice[2] == dice[3] and dice[3] == dice[4]):
    return 25
  else:
    return 0
#Small straight = 30
#Given a sorted array of 5 dice values, returns 30 if a small straight or zero.
def smallStraight (dice):
  if (dice[0]+1 == dice[1] and dice[1]+1 == dice[2] and dice[2]+1 == dice[3]):
    return 30
  elif (dice[1]+1 == dice[2] and dice[2]+1 == dice[3] and dice[3]+1 == dice[4]):
    return 30
  else:
    return 0
#Large straight = 40
#Given a sorted array of 5 dice values, returns 40 if a large straight or zero.
def largeStraight (dice):
  if (dice[0]+1 == dice[1] and dice[1]+1 == dice[2] and dice[2]+1 == dice[3] and dice[3]+1 == dice[4]):
    return 40
  else:
    return 0
#Yahtzee (5 of a kind) = 50
#Given an array of 5 dice values, returns 50 if a five of a kind or zero.
def yahtzee (dice):
  if (dice[0] == dice[1] and dice[1] == dice[2] and dice[2] == dice[3] and dice[3] == dice[4]):
    yahtzeeFlag = True
    return 50
  else:
    return 0

#Joker Rule allows subsequent Yahtzees to score in any field using normal rules.
#What I might do here is define a joker function that sets values to joker rules and run the above "else" returns through it to check for an additional yahtzee
#Each subsequent yahtzee also earns an additional 100 points.
#Scoring at least 63 in the upper portion earns an additional 35 points.
