
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days=0
    assert(dayBeforeNext(year1,month1,day1,year2,month2,day2) > 0)
    while (dayBeforeNext(year1, month1,day1, year2, month2, day2)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days+=1
    return days

def nextDay(year, month, day):

    # Returns the year, month, day of the next day.

    if (day < daysInMonth(month,year)):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dayBeforeNext(year1, month1, day1, year2, month2, day2):
    if (year1 < year2):
        dbn=True
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

def daysInMonth(month,year):
    if (month == 2):
        days = 28 + isLeapYear(year)
    else:
        days = 31 - (month - 1) % 7 % 2
    return days

def isLeapYear(year):
    if ((year % 4 == 0) | ((year % 100 == 0) & (year % 400 == 0))):
        leapYear = 0
    else :
        leapYear = 1
    return leapYear


print nextDay(2012,4,30)
print daysBetweenDates(2011,1,1,2012,8,8)
#print daysInMonth(4)