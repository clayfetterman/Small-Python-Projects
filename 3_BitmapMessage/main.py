"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays text over a pattern, which is hard-coded into the code."""

# no main entry point
#sys: standard libary module
import sys

#hard-code image below
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message: Program 3')
print('Enter the message to display over the bitmap.')

#Altered code to loop until input is entered, not exit the program
message = ''
while message == '':
    print('Enter the message to display over the bitmap.')
    message = input('> ')


#.splitlines(): string method that splits a string into a list of lines:
#splits where there is a newline
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            #simple but non-intuitive way to cycle through all chars in message
            print(message[i % len(message)], end='')
    print()