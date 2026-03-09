"""Carrot in a Box, by Al Sweigart al@inventwithpython.com"""
# Clay Fetterman, 03/09/2026 Project 9
# Two player game with 2 boxes, once of which has a carrot.
# The first player looks in their box, and then tells the second player if
# their box contained the carrot.
# The second player then chooses whether to swap boxes
# The boxes are opened, and the player with the carrot wins

import random
print('Carrot In A Box Game!')











input('Press Enter to begin...')

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11) + '    ' + p2Name[:11].center(11) #print names centered in 11 chars

print('''HERE ARE TWO BOXES:
    __________     __________
   /         /|   /         /|
  +---------+ |  +---------+ |
  |   RED   | |  |   GOLD  | |
  |   BOX   | /  |   BOX   | /
  +---------+/   +---------+/''') # copied form online repo: I'm not recreating that

print()
print(playerNames)
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')
print()
print(p1Name + ', you will get to look into your box.')
print(p2Name.upper() + ', close your eyes and don\'t look!')
input('When ' + p2Name + ' has closed their eyes, press Enter...')
print()

print(p1Name + ' here is the inside of your box:')

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    if carrotInFirstBox:
        print('''
         ___VV____
        |   VV    |
        |   VV    |
        |___||____|    __________
       /    ||   /|   /         /|
      +---------+ |  +---------+ |
      |   RED   | |  |   GOLD  | |
      |   BOX   | /  |   BOX   | /
      +---------+/   +---------+/
       (carrot!)''')
        print(playerNames)
    else:
        print('''
         _________
        |         |
        |         |
        |_________|    __________
       /         /|   /         /|
      +---------+ |  +---------+ |
      |   RED   | |  |   GOLD  | |
      |   BOX   | /  |   BOX   | /
      +---------+/   +---------+/
      (no carrot!)''')

        print(playerNames)

print('\n' * 100) # clear the screen
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue...')

print()
print(p1Name + ', say one of the following to ' + p2Name + ':')
print(' 1) There is a carrot in my box.')
print(' 2) There is not a carrot in my box.')
print()
input('Then press Enter to continue...')

print()
print(p2Name + ', do you want ot swap boxes with ' + p1Name + '? YES/NOT')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('YES')):
        print(p2Name + ', please enter "YES" or "NO".')
    else:
        break

firstBox = 'RED ' # SPACE AFTER 'D'
secondBox = 'GOLD'

if response.startswith('Y'):
    carrotInFirstBox = not carrotInFirstBox   # big 'ole variable swaps
    firstBox, secondBox = secondBox, firstBox # big 'ole variable swaps

print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Press Enter to reveal the winner...')
print()

if carrotInFirstBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)


if carrotInFirstBox:
    print(p1Name + ' is the winner!')
else:
    print(p2Name + ' is the winner!')

print('Thanks for playing!')


'''
Project Q and A's:
    1) What happens if you enter a name longer than 11 chars?
        It will display the full name, overwriting 11 evenly on both sides
    2) What happens if you omit the space at the end of "firstBox = 'RED ' on line 103?
        Misalignment: RED has 3 letters, GOLD has 4
    3) What happens if you delete or comment out print(*'\n' *100) on line 83?
        This provides spacing to hide results from Player 2 when they open their eyes
    4) What happens if you delete or comment out the else: on line 100 and break on line 101?
        infinite loop!
'''