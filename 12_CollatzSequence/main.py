# Collatz Sequence, by Al Sweigart al@inventwithpython.com
'''
Clay Fetterman, 03/10/2026, Project 12
This is a math formula that (unproven) will always eventually end in a 1. Simple math implementation.
3n + 1:
    1) if n is even, n = n/2
    2) if n is odd, n = n*3+1
    3) if n = 1, stop
'''
import sys, time
print('''Colatz Sequence: the 3n + 1 Problem
    This is a math formula that (unproven) will always eventually end in a 1.
    3n + 1:
        1) if n is even, n = n/2
        2) if n is odd, n = n*3+1
        3) if n = 1, stop''')






print('Enter a starting number that is > 0:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.') # .isdecimal() checks for 0-9, else it fails (- catch)
    sys.exit() # no looping here: gotta rerun 

n = int(response)
print(n, end='', flush=True) # flush bypasses output buffer: not sure why it is required here...
while n != 1:
    if n % 2 == 0:
        n = n // 2 # recall: // always returns whole number (rounded up)
    else:
        n = n // 3 + 1

    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()