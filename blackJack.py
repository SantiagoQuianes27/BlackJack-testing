import time, os, random

# The code below sets the starting values before the game 
chips = 2000
hand = 0
dealerHand = 0
bet = 0
# this calls the while true function
blackJack = True
# below will the new commands for the processes to be much simpler by calling it and all the math and 
# commenting being done here rather than constantly repeating it down in the code
def lose ():
  global chips

  lostMessage = random.randint(1,5)
  chips -= bet

  if lostMessage == 1:
    print("hey you lost heres your chips: ", chips)
  elif lostMessage == 2:
    print("this is message 2, chips: ", chips)
  elif lostMessage == 3:
    print("this is message 3, chips: ", chips)
  elif lostMessage == 4:
    print("this is message 4, chips: ", chips)
  else:
    print("this is message 5 or something went wrong, chips: ", chips)

  return chips

while blackJack is True:
  bet = int(input("Place your bet: "))
  time.sleep(2.5)
  lose()
  time.sleep(4)
  continue