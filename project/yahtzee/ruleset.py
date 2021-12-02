
#Yahtzee has two sections, an upper section and a lower section.

#Upper section only counts dice that match the descriptor or are zero

#Given an array of dice values and a desired pip value, returns sum of all die with desired pip value
def sumVals (dice, val):
  sum = 0
  for x in dice:
    if x == val:
      sum += val
  return sum

#Lower section has more complex rules
#If there are three of a kind, the score returned is 
