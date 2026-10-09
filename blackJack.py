import time, os, random, math

# The code below sets the starting values before the game 
chips = 2000

# this calls the while true function
blackJack = True

# below will the new commands for the processes to be much simpler by calling it and all the math and 
# commenting being done here rather than constantly repeating it down in the code. the lost and win will be calculated here

def lose ():
  global chips

  lMessage = random.randint(1,5)
  chips -= bet

  if lMessage == 1:
    print("hey you lost heres your chips: ", chips)
  elif lMessage == 2:
    print("this is message 2, chips: ", chips)
  elif lMessage == 3:
    print("this is message 3, chips: ", chips)
  elif lMessage == 4:
    print("this is message 4, chips: ", chips)
  else:
    print("this is message 5 or something went wrong, chips: ", chips)

  return chips

def win ():
  global chips

  wMessage = random.randint(1,5)
  chips += bet

  if wMessage == 1:
    print("hey you won heres your chips: ", chips)
  elif wMessage == 2:
    print("this is win message 2, chips: ", chips)
  elif wMessage == 3:
    print("this is win message 3, chips: ", chips)
  elif wMessage == 4:
    print("this is win message 4, chips: ", chips)
  else:
    print("this is win message 5 or something went wrong, chips: ", chips)



while blackJack is True:
  # Inside the while true loop these variables will stay as to reset the game everytime without affecting the chips after you've betted
  hand = 0
  dealerHand = 0
  bet = 0
  #This clears the Terminal before starting the next game
  os.system("clear")

#This is the betting process below which does not allow for the value of bet to be greater than the amount of chips you have
  bet = float(input("Place your bet: "))
  bet = int(bet)
  time.sleep(0.5)
  os.system("clear")
  
#The code ensures you dont continue the game without inputing the correct value, restarting you from the top but not affecting your total chips
  if bet <= 0:
    print("\033[31mSTOP TRYING TO ROB US!\033[0m")
    time.sleep(0.5)
    os.system("clear")
    continue
  elif bet > chips:
    print("Thats more than you have bud remember you have:", chips)
    time.sleep(3)
    continue

  time.sleep(2.5)
  win()
  time.sleep(4)
  continue