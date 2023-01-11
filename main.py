print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Hunt.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

side = input('You\'re at a crossroad, choose "right" or "left" to go:\n')
side_lower = side.lower()
if side_lower != 'left':
  print("\nYou fought a dragon and lost. Game over!")
if side_lower == 'left':
  river = input('\nNow you\'re in front of a river, do you choose to "swim" or "wait" for a boat?\n')
  river_lower = river.lower()
  if river_lower != 'wait':
    print("\nYou were attacked by a river monster. Game over!")
  if river_lower == 'wait':
    door = input('\nA boat has arrived to take you, the boatman tells you that those waters are treacherous and hide many unknown things and that thankfully you decided not to swim.\n You\'ve reached the other side of the river. Now you\'re in front of a house with three doors: red, yellow and blue. Which one do you choose?\n')
    door_lower = door.lower()
    if door_lower == 'red':
      print("\nYou walked into a room full of baby dragons and got burned. Game over!")
    elif door_lower == 'blue':
        print("\nYou\'ve entered the house of a evil magus. Game over!")
    elif door_lower == 'yellow':
      print("\nYou entered a room with three chests and each of them has a message:\n")
      print("Chest 1 - When you least expect it you can find me.\n")
      print("Chest 2 - Does a star shine like gold or like fire?\n")
      print("Chest 3 - From a distant land, but not very habitable.\n")
      chest = int(input("Which one do you choose? 1, 2 or 3?\n"))
      if chest == 1:
        print("\nThe magus\' spell disintegrate you. Game over!")
      elif chest == 2:
        print("\nThe magus\' spell burns you. Game over!")
      elif chest == 3:
        print("\nYou found the treasure! Congratulations you win!") 
      else:
        print("\nMaybe you didn't pay enough attention. Game over!'")
    else:
      print("\nWhat were you trying to do? Game over.")