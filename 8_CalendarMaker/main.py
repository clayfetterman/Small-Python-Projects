# Calendar Maker, by Al Sweigart al@inventwithpython.com
# Clay Fetterman, 03/03/2026
# get a year and month from the user, and generate an ASCII calendar with
# correct days for that month. Utilizes Python's datetime module
# Remember: module < package < library

import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')


print('Calendar Maker')
# get year from user
while True:
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2026.')
    continue
# get month form user
while True:
    print('Enter the numeric month for the calendar:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month (1-12)')
        continue

    month = int(response)
    if 1 <= 12:
        break



# generate the calendar based on year/month provide by user
def getCalendarFor(year, month):
    calText = '' # the ASCII calendar

    # print month and year at top of calendar
    calText += (' ' * 34) + MONTHS[month -1] + ' ' + str(year) + '\n'


    # add days of the week labels to calendar
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # build: horizontal lines
    weekSeparator = ('+----------' * 7) + '\n'

    # build: empty space in days
    blankRow = ('|          ' * 7) + '|\n'


    # use datetime module to get first day of that given year/month
    currentDate = datetime.date(year, month, 1)


    # roll back day of week from current day until 1st Sunday (start of calendar)
    while currentDate.weekday() != 6: # Sunday returns 6
        currentDate -= datetime.timedelta(days=1) # setting unit as days, value as 1: see module for function details

    while True:
        calText += weekSeparator

        # build the day number row within the calendar blocks
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        # build the calendar blocks from the day number row and black rows
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # was that the last day of the month?
        if currentDate.month != month:
            break

    # build bottom line of calendar
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)

# bonus: save to file
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj: # open a file for writing
    fileObj.write(calText) # fileObj is just a variable name for the object returned by open()

print('Saved to ' + calendarFilename)

'''
Knowledge Checks
    1. How can you make the calendar display abbreviated months?
        A) Change the days string: will also need to adjust spacing
    2. What error message do you get if you delete or comment out year = int(response) on line 21?
        A) All user input comes in as a string, so if it isn't changed to an int it will return errors
            when using as input for datetime calls
    3. How can you make the calendar not display the days of the week at the top?
        A) Remove the string and/or don't add it to the calendar building
    4. How can you make the program not save the calendar to a file?
        A) Remove the open() function and associated write
    5. What happens if you delete or comment out print(calText) on line 93?
        A) You get no calendar on STDOUT: file write will still work, though
'''
