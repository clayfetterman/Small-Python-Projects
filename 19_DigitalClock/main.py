"""

Clay Fetterman, 03/031/2026: Project 19: Digital Clock
    This is essentially a repeat of Project 14, but pulls in the real-time clock of the host system.
    As with Project 14, it uses the "sevseg.py" module from Project 64, which does most of the heavy lifting
    in providing the correct symbols to build the display.
"""

import sys, time, sevseg

try:
    while True:
        print('\n' * 60)

        # Pull host system time and set variables for syseg module (I changed to 24 hour instead of 12)
        currentTime = time.localtime()
        hours = str(currentTime.tm_hour % 24)
        if hours == '0':
            hours = '24'
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Get symbols based on time for sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Display the results
        print(hTopRow + '     ' + mTopRow + '     ' + sTopRow)
        print(hMiddleRow + '  *  ' + mMiddleRow + '  *  ' + sMiddleRow)
        print(hBottomRow + '  *  ' + mBottomRow + '  *  ' + sBottomRow)

        # Update roughly every second: holds until second passes then re-executes the main 'True'
        while True:
            time.sleep(0.1)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

except KeyboardInterrupt:
    print('Goodbye!')
    sys.exit()