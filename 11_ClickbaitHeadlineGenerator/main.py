# Clickbait Headline Generate by Al Sweigart, al@inventwithpython.com
# Clay Fetterman, 03/10/2026, Project 11
# Uses pre-created lists of parts of speech, and 8 separate "types" of headlines
# It is a pretty straightforward program: more hardcoding than creativity. Neat though!
# Each headline type is a standalone function: building blocks are global
import random

# Copied below arrays
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():
    print('Clickbait Headline Generator')

    print()

    print('Our website needs slop content!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number')
        else:
            numberOfHeadlines = int(response)
            break

    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1,8)

        if clickbaitType == 1:
            headline = generateAreMillennialsKillingHeadline()
        elif clickbaitType == 2:
            headline = generateWhatYouDontKnowHeadline()
        elif clickbaitType == 3:
            headline = generateBigCompaniesHateHerHeadline()
        elif clickbaitType == 4:
            headline = generateYouWontBelieveHeadline()
        elif clickbaitType == 5:
            headline = generateDontWantYouToKnowHeadline()
        elif clickbaitType == 6:
            headline = generateGiftIdeaHeadline()
        elif clickbaitType == 7:
            headline = generateReasonsWhyHeadline()
        elif clickbaitType == 8:
            headline = generateJobAutomatedHeadline()

        print(headline)
    print()

    website = random.choice(['obsite', 'blag', 'Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram'])

    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, 'to bring in those sweet clicks!')


# Functions for the 8 diff types of headline generations
def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killing hte {} Industry?'.format(noun)


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, pluralNoun, when)


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return 'You Won\'t Believe What This {} {} Found in {} {}'.format(state, noun, pronoun, place)


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return 'What {} Don\'t Want You To Know About {}'.format(pluralNoun1, pluralNoun2)


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number, noun, state)


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    # make number 2 larger than 1
    number2 = random.randint(1, number1)
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1,pluralNoun,number2)
def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = POSSESIVE_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} Didn\'t Think Robots Would Take {} Job. {} Were Wrong.'.format(state, noun, pronoun1, pronoun2)
    else:
        return 'This {} {} Didn\'t Think Robots Would Take {} Job. {} Was Wrong.'.format(state, noun, pronoun1, pronoun2)

# set jump into main
if __name__ == '__main__':
    main()

'''
Program Q and A:
    1) What error message do you get if you delete or comment out numberOfHeadlines = int(response) on line 34
        User input is always a string: need an int for the loop count
    2) What error message do you get if you change int(response) to response on line 34?
        numberOfHeadlines becomes a string: same error as Q 1
    3) What error message do you get if you change line 19 to WHEN = []?
        Error from emtpy sequence
'''
