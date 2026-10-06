import time, os, random

# The code below sets the starting values before the game 
chips = 2000
hand = 0
dealerHand = 0
bet = 0
# this calls the while true function
blackJack = true
# below will the new commands for the processes to be much simpler by calling it and all the math and 
# commenting being done here rather than constantly repeating it down in the code
def lose ():
  global chips
  chips -= bet:

