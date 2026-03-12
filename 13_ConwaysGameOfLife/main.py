"""
Conway's Game of Life, by Al Sweigart al@inventiwthypthon.com
Clay Fetterman, 03/11/2026, Project 13
Conway's game is a simulation of cells in a grid, with follow these rules for each round:
1. Living cells with two or three neighbors stay alive
2. Dead cells with exactly 3 living neighbors become alive
3. Any other cell dies or stays dead
"""

import random, copy, sys, time

# Set up grid
WIDTH = 79
HEIGHT = 20
ALIVE = '0'
DEAD = ' '



# Store current and next state for cells in a dictionary tuple


nextCells = {}
# Fill out initial state (randomly): 50/50 chacne of cell starting alive or dead
for x in range(WIDTH):
    for y in range(HEIGHT):

        if random.randint(0,1) == 0:
            nextCells[x,y] = ALIVE
        else:
            nextCells[x,y] = DEAD
# enter main: each loop is 1 round of simulation
while True:


    print('\n' *50)
    cells = copy.deepcopy(nextCells) # Creates a stand alone copy: simple x = y references the same dictionary!

    # Print the cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x,y], end=' ')
        print()
    print('Press Ctrl-C to quit.')

    # Calculate each cell for the next round using the simulation roles in intro
    for x in range(WIDTH):
        for y in range(HEIGHT):

            # IMPORTANT: the Modulus applies wrap around capability: error elsewise
            # Consider: (-1) % 50 -> 49: wraps left side to right edge
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT # Remember that Y coordinates are inverted! Remember DVD project
            below = (y + 1) % HEIGHT # Remember that Y coordinates are inverted! Remember DVD project

            # Check all neighbors (8 of them)
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            # Update next Cell status
            if cells[(x,y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):


                nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbors == 3:

                nextCells[(x,y)] = ALIVE
            else:

                nextCells[(x,y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('Conway\'s Game of Life')
        sys.exit()