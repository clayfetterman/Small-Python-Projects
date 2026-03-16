"""
Dice Math by Al Sweigart, al@inventwithpython.com
Clay Fetterman, 03/16/2026, Project 17

This rolls several dice, and the user has a limited time to add up the numbers. The ASCII dice art and randomized
landings are the neat part, but a real pain.
    Learned assert: (is True?)
    Learned enumerate(): returns both the index and value of each item as it is looped through
"""
import random, time
# Set up constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3 # This leaves space for the user to enter the total

QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6


REWARD = 4
PENALTY = 1



#  assert is basically (is True?). If not, it halts the program
assert MAX_DICE <= 14 # error check: too many dice will crash the program (not enough space to display)
# I copied all of this ASCII art over
D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

# Some dice have different depictions due to non-symmetrical pips
ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math

Add up all values displayed on the dice before time runs out. You have {} seconds!
You get {} points for each correct answer, but lose {} for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to roll the dice...')

# Track Points
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:

    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die = random.choice(ALL_DICE) # Add dice tuple (ASCII, value) to die
        diceFaces.append(die[0]) # Append die[0] to diceFaces (the ASCII art)
        sumAnswer += die[1] # Track the sum (1 is the value part of the tuple)


    # This will be the x/y coordinates of the top left corner of dice: used to print out the rest
    topLeftDiceCorners = []


    # Calculate the various die locations / check for overlaps
    for i in range(len(diceFaces)):
        while True:
            # Choose a random start point for top-left corner: gotta leave room, too
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # Set the Die corner locations
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT # Remember that in Python, Y coordinates increase going down
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # Check for Overlaps
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT

                # Check if current die is located in space of previous die
                for cornerX, cornerY in ((topLeftX, topLeftY), (topRightX, topRightY), (bottomLeftX, bottomLeftY), (bottomRightX, bottomRightY)):
                    if prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom:
                        overlaps = True

            if not overlaps:
                topLeftDiceCorners.append((left, top))
                break

    # Print the dice
    # This rolls through the ASCII art as an x/y coordinate to print the die
    canvas = {}
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = dieLeft + dx
                canvasY = dieTop + dy
                canvas[(canvasX, canvasY)] = dieFace[dy][dx] # Lists are row, then column: the ASCI art checks the Y, THEN X!!

    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), ' '), end='')
        print()

    # Get player input
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Incorrect...')
        time.sleep(2)
        incorrectAnswers += 1

# Display Score
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct:   ', correctAnswers)
print('Incorrect: ', incorrectAnswers)
print('Score:     ', score)