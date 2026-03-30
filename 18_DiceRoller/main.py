"""
Dice Roller, by Al Sweigar al@inventwithpython.com
Clay Fetterman, 03/30/2026: March 30/26
    Dice Roller: User inputs number of and type of dice, and program provides results.
    Lots of input validation / parsing. Dice rolls are trivial.
    New method of error handling learned here: can treat exceptions as a variable.

    I found one issue in the original code: if you chose both +- multipliers (i.e. 10d6+-10)
        it will default to addition. If you do -+ however, it raises an exception.
        This is because the code checks for a '+', and if not found, assigns a '-'.
        I added code to the 'Get modifier' section to check for multiple '+' and '-', or both.
"""

import random, sys

print("Dice Roller")
print("Enter the number of and type of dice you wish to roll..")
print("i.e.: 1d12, 2d6, or even 100d25! You an also add adjustments (2d6+2)")
print("Enter \"quit\" to end program.")

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == 'QUIT':
            print("Goodbye!")
            sys.exit()

# Input Parsing
        # Remove any spaces from input
        diceStr = diceStr.lower().replace(' ', '')

        # Locate 'd' from input
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the number of dice')

        # Get number of dice from input
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice')
        numberOfDice = int(numberOfDice)

        # Get modifier from input (are we adding or subtracting?)
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')
        # My added error handling (multiple +'s or -'s)
        plusCount = diceStr.count('+')
        minusCount = diceStr.count('-')
        if plusCount > 1 or minusCount > 1 or (plusCount == 1 and minusCount == 1):
            raise Exception('Too many modifier values!')

        # Get number of sides of dice from input
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the nubmer of sides')
        numberOfSides = int(numberOfSides)

        # Get modifier amount from input
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                modAmount = -modAmount

# Generate Dice Rolls: the printout is a messy mix of non-newline print statements
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        print('Total:', sum(rolls) + modAmount, '(Each die:', end='')

        # Display individual rolls
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

# Error Handing
    except Exception as exc:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue







