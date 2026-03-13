'''
Diamonds, by Al Sweigart, al@iventwithpython.com
Clay Fetterman, 03/13/2026, Project 16
This one is simple ASCII art that draws outline/filled diamonds based on size number
The parts of the diamond are created via their representation to the size number
    I edited it so the user chooses the size*
'''






def main():
    print('Diamond Printer')
    print()
    # Get user input
    while True:
        print("Enter a size value (int): ")
        response = input('>')
        if not response.isdecimal():
            print('Invalid input: enter an integer please')
        else:
            response = int(response)
            break
    # Call the functions to draw the Diamonds
    displayOutlineDiamond(response)
    print()
    displayFilledDiamond(response)


# Functions to draw Diamonds
def displayOutlineDiamond(size):
    # Print Top Half
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end ='')
        print('\\')
    # Print Bottom Half
    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * ((size - i -1) * 2), end='')
        print('/')


def displayFilledDiamond(size):
    # Print Top Half
    for i in range(size):
        print(' ' * (size -i -1), end='')
        print('/' * (i+1), end='')
        print('\\' * (i + 1))
    #Print Bottom Half
    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))




# If this program was run isntead of imported
if __name__ == '__main__':
    main()