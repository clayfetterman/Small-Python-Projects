"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com"""
#uses bext.goto() for logo location
#logos are dictionaries
# "A cross-platform Python 2/3 module for colorful, boring, text-based terminal programs."
# HA




import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module')
    print('Install by following instructions at')
    print('https://pypi.python.org/pypi/bext')
    sys.exit()


WIDTH, HEIGHT = bext.size()

#printing to the final column on Windows adds a newline by default: this avoids that
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)


COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    #create logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH -4),
            Y: random.randint(1, HEIGHT -4),
            DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            #set X to even so it can hit the corner
            logos[-1][X] -= 1

    cornerBounces = 0
    while True:
        for logo in logos:
            #erase logo's current location
            bext.goto(logo[X], logo[Y])
            print('   ', end='')

            originalDirection = logo[DIR]

            #check for corner bounce
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            #check for left edge bounce
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            #check for right edge bounce
            #WIDTH - 3 for three characters in DVD
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            #check for top edge bounce
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            #check for bottom edge bounce
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            #change color on any bounce
            if logo[DIR] != originalDirection:

                logo[COLOR] = random.choice(COLORS)

            #Logo move: (remember, bext() Y is positive as it goes down)
            #X needs to move by 2 because Chars are twice as tall as wide
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1


        bext.goto(5, 0)
        bext.fg('white')
        print('Corner Bounces:', cornerBounces, end='')

        for logo in logos:
            #draw logos
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0,0)
        #this is required for bext
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo')
        sys.exit() #handles CNTRL+C interupt to exit program

