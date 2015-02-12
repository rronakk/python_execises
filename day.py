print "Enter Your birth date in following format : yyyy/mm/dd "
birthDate = raw_input('>')
print" Enter current date in following format : yyyy/mm/dd "
currentDate = raw_input('>')

year1, month1, day1 = birthDate.split("/")
year2, month2, day2 = currentDate.split("/")

year1 = int(year1)
month1 = int(month1)
day1 = int(day1)

year2 = int(year2)
month2 = int(month2)
day2 = int(day2)


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # Counts total number of days between given dates

    days = 0
    assert(dayBeforeNext(year1, month1, day1, year2, month2, day2) > 0)
    while (dayBeforeNext(year1, month1, day1, year2, month2, day2)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def nextDay(year, month, day):

    # Helper function to return the year, month, day of the next day.

    if (day < daysInMonth(month, year)):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dayBeforeNext(year1, month1, day1, year2, month2, day2):

    # Validates if user has not entered future date before past date

    if (year1 < year2):
        dbn = True
    elif(year1 == year2):
        if(month1 < month2):
            dbn = True
        elif(month1 == month2):
            if(day1 < day2):
                dbn = True
            else:
                dbn = False
        else:
            dbn = False
    else:
        dbn = False
    return dbn


def daysInMonth(month, year):

    # Calculate days in a given month and year
    # Algorithm used for reference : http://www.dispersiondesign.com/articles/time/number_of_days_in_a_month

    if (month == 2):
        days = 28 + isLeapYear(year)
    else:
        days = 31 - (month - 1) % 7 % 2
    return days


def isLeapYear(year):

    # Determine if give year is lear year or not.
    # Algorithm used for reference : http://www.dispersiondesign.com/articles/time/determining_leap_years
    """
    if ((year % 4 == 0) or ((year % 100 == 0) and (year % 400 == 0))):
        leapYear = 1
    else:
        leapYear = 0
    return leapYear
    """
    if (year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                leapYear = 1
            else:
                leapYear = 0
        else:
            leapYear = 1
    else:
        leapYear = 0

    return leapYear

print "=============================================================== \n Your age in days is : %d " % daysBetweenDates(year1, month1, day1, year2, month2, day2)