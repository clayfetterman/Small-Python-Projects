"""
Countdown, by Al Sweigart al@inventwithpython.com
Clay Fetterman, 03/11/2026: Project 13
Uses the sevseg module to convert user input numbers to a digital clock display
    which will continously count down to 0:0:0
    sevseg.py (Project 64) copied from online repo
"""


import sys, time, sevseg

# I created the below to allow user input for time
while True:
    print("Enter in a number for the countdown (seconds):")
    response = input('< ')

    if not response.isdecimal():
        print("You must enter an integer.")
    else:
        response = int(response)
        break
# main program loop
try:
    while True:
        hours = str(response // 3600) # won't handle times > 99 hours!!
        minutes = str(response % 3600 // 60)
        seconds = str(response % 60 % 60)


        # use the sevseg module to print the timer
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Print Display
        print(hTopRow + '       ' + mTopRow + '       ' + sTopRow)
        print(hMiddleRow + '   *   ' + mMiddleRow + '   *   ' + sMiddleRow)
        print(hBottomRow + '   *   ' + mBottomRow + '   *   ' + sBottomRow)

        if response == 0:
            print()
            print('BOOOOOOM!')
            break

        print()
        time.sleep(1)
        response -= 1

except KeyboardInterrupt:
    print('Countdown Timer')
    sys.exit()







