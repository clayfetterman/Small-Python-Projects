#Caesar Cipher hacker, by Al Sweigart al@inventwithpython.com
#Clay Fetterman, 03/03/2026, Project 7
# Uses brute force to display all possible decryptions of the Caesar Cipher to a user supplied
# string (26 total keys). Results are obvious to operator with key is correct.




print('Caesar Cipher Hacker, by Al Sweigart al@inventwithpython.com')

# get user input of encrypted message
print('Enter the encrypted Caesar Cipher Text')
message = input('> ')

# create "library" for decryption algo

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    # decryption algo
    for symbol in message:
        if symbol in SYMBOLS: # ignores non-alpha chars
            num = SYMBOLS.find(symbol) #return char # within SYMBOLS
            num = num - key

            # handle wrap-around
            if num < 0:
                num = num + len(SYMBOLS)

            # swap based on num/key
            translated = translated + SYMBOLS[num]
        else: # ignores non-alpha chars

            translated = translated + symbol

    # output
    print('Key #{}: {}'.format(key, translated))

