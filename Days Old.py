# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    return days_passed(year2,month2,day2)-days_passed(year1,month1,day1)

def isLeapYear(year):
    if year%4==0:
        if year%400==0:
            return True
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
    if year%4==0:
        if year%100==0:
            if year%400!=0:
                return False
    if year%4==0:
        return True
    else:
        return False

def days_in_year(year):
    if isLeapYear(year):
        return 366
    else:
        return 365

def get_days(year,month):
    if month==1:
        return 31
    if month==2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    if month==3:
        return 31
    if month==4:
        return 30
    if month==5:
        return 31
    if month==6:
        return 30
    if month==7:
        return 31
    if month==8:
        return 31
    if month==9:
        return 30
    if month==10:
        return 31
    if month==11:
        return 30
    if month==12:
        return 31

def days_passed(year,month,day):
    i=1
    result=day
    while i!=month:
        result=result+get_days(year,i)
        i=i+1
    counter=0
    years_days=0
    while counter!=year:
        years_days=years_days+days_in_year(counter)
        counter=counter+1
    return result+years_days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")

test()

