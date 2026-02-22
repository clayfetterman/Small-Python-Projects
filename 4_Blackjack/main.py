"""Blackjack, by Al Sweigart al@inventwithpython.com

My note: great way to implement the deck: better than brute force creation (though LLM makes it trivial to do)
I like using double-quotes for literal words, output and single for other: probably should stick to one"""






import random, sys

#create suit images (chr(XXX)) are the emojis
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'



def main():
    print('''Blackjack, by Al Sweigart al@inventwithpython.com''')

    print("Rules: you know how to play Blackjack :)")











    money = 5000
    while True:
        if money <= 0:
            print("You\'ve gone bust!")



            sys.exit()


        print("Money:", money)
        bet = getBet(money)

        #deal the cards
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]


        #resolve player actions
        print("Bet:", bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()


            if getHandValue(playerHand) > 21:
                break


            move = getMove(playerHand, money - bet)


            if move == 'D':
                #KFC double-down!
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:", bet)

            if move in ('H', 'D'):
                #hit and KFC double-down!
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}.".format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue


            if move in ('S', 'D'):
                #stand and KFC double-down!
                break

            #resolve dealer actions
            if getHandValue(playerHand) <= 21:
                while getHandValue(dealerHand) < 17:

                    print("Dealer hits...")
                    dealerHand.append(deck.pop())
                    displayHands(playerHand, dealerHand, False)

                    if getHandValue(dealerHand) > 21:
                       break
                    input("Press Enter to continue...")
                    print("\n\n")

        #Show final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        if dealerValue > 21:
            print("Dealer goes bust! You in ${}!.".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You've lost, sorry :(")
            money -= bet
        elif playerValue > dealerValue:
            print("You've won ${}.".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie: the bet is returned to you")

            input("Press Enter to continue...")
            print("\n\n")

#get the players bet
def getBet(maxBet):

    while True:
        print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
        bet = input('> ').upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet  <= maxBet:
            return bet

#create the deck of cards: use stack.pop() to deal them
def getDeck():

    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

#display player and dealer hands,  hiding 1st dealer card as option
def displayHands(playerHand, dealerHand, showDealerHand):


    print()
    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        #hide dealers 1st card: then slice dealerHand from start to index 1 to end (1, X, X): so first card is ignored (hidden)
        displayCards([BACKSIDE] + dealerHand[1:])


        print("PlAYER: ", getHandValue(playerHand))
        displayCards(playerHand)

#get the count of the hand
def getHandValue(cards):


    value = 0
    numberOfAces = 0

    #get value of non-Ace cards
    for card in cards:
        rank = card[0] #remember a card is a tuple! (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    #handle Ace's value: add 11 is possible, else leave at 1
    value += numberOfAces
    for i in range(numberOfAces):

        if value + 10 <= 21:
            value += 10

    return value

#show hands using ASCII Art
def displayCards(cards):
    rows = ['', '', '', '', ''] #five cards per hand max

    for i, card in enumerate(cards):
        rows[0] += '__ '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|## | '
            rows[3] += '|## | '


        else:

            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))


    for row in rows:
        print(row)

#resolve player input/actions
def getMove(playerHand, money):


    while True:

        moves = ['(H)it', '(S)tand']



        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')


        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move



if __name__ == '__main__':
    main()