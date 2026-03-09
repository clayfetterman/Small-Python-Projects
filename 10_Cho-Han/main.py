# Cho-Han, by Al Sweigart al@inventwithpython.com

# Clay Fetterman, 03/09/2026, Project 10
# Two dice are rolled, guess Cho (even) or Han (odd) for the total

import random, sys

JAPANESE_NUMBERS = {1: "ICHI", 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}


print('Cho-Han! Let\'s play!')






purse = 5000
while True:
    # place bet
    print('You have ', purse, 'mon. How much do you want to bet? (or QUIT)')
    while True:
        pot = input('> ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing, Goodbye!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number')
        elif int(pot) > purse:
            print('You do not have enough to make that bet!')
        else:

            pot = int(pot)
            break

    # roll dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice...')
    print('The dealer slams the cup on the floor, still covering the dice...')
    print('The dealer looks at you: "Cho (even) or Han (odd)"?')
    print()


    # Place bet on Cho or Han
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN"')
            continue
        else:
            break

    # Reveal dice results
    print('The dealer lifts the cup to reveal...')
    print('    ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('       ', dice1, '-', dice2)

    # Determine if player won or lost
    rollIsEven = (dice1+dice2) % 2 == 0
    if rollIsEven:
        correctBet = ('CHO')
    else:
        correctBet = ('HAN')

    playerWon = bet == correctBet # interesting way to do this

    # Display results
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        print('The house collets a', pot // 10, 'mon fee') # // divides and rounds to nearest whole number
        purse = purse - (pot // 10)
    else:
        print('You lost!')
        purse = purse - pot

    # Is player bust?
    if purse == 0: # they can't bet more than they have
        print('You\'ve gone bust!')
        print('Thanks for playing, Goodbye!')
        sys.exit()


