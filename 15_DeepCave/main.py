"""
Deep Cave, by Al Sweigart al@inventwithypython.com
Clay Fetterman, 03/12/2026, Project 15

This program prints news lines of organized "walls" and spaces mimicking a hole, and
scrolls on and on...nothing fancy, but a neat little program.
"""
import random, sys, time
# Set up vars
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deeeeep Caaaaave')
print('Press CTRL+C to Quit')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Print the tunnel
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    #Check for the keyboard interupt
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    # Adjust the left tunnel wall
    diceRoll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH -1:
        leftWidth = leftWidth + 1
    else:
        pass

    # Adjust the gap

    diceRoll = random.randint(1,6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1
    else:
        pass