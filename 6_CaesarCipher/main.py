
"""Caesar Cipher, by Al Sweigart al@inventwithpython.com"""
# Clay Fetterman 03/02/2026: Project 6



# pyperclip copies text to host clipboard: if install fails, do nothing
try:
    import pyperclip
except ImportError:
    pass



# All alphabet chars
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher')
print('Encyption by shifting alphabet X values to the right (decrypt to the left)')
print()



# user choose encrypt or decrypt
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter \'e\' or \'d\'')

# user chooses key size
while True:
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key size (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) <= len(SYMBOLS):
        key = int(response)
        break

# user chooses message
print('Enter the message to {}.'.format(mode))
message = input('> ')


message = message.upper()


translated = ''

# encrypt/decrypt time!
for symbol in message:
    if symbol in SYMBOLS:

        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key


# error handling
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)


        translated += SYMBOLS[num]
    else:
        # Char wasn't in alphabet: leave as is
        translated += symbol

# return en/decrypted message
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass