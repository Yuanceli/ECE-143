import calendar
def number_of_days(year, month):
    '''
    returns the number of calendar days in a given year and month.
    '''
    assert isinstance(year, int) and isinstance(month, int)
    assert year >= 0 and 1 <= month <= 12
    a, b = calendar.monthrange(year, month)
    return b

def number_of_leap_years(year1, year2):
    '''
    find the number of leap-years between (including) two given years.
    '''
    assert isinstance(year1, int) and isinstance(year2, int)
    assert 0 <= year1 <= year2
    n = calendar.leapdays(year1, year2)
    if calendar.isleap(year2):
        n += 1
    return n

def get_day_of_week(year, month, day):
    '''
    find the string name of the day of the week on a given month,day, and year.
    '''
    assert isinstance(year, int) and isinstance(month, int) and isinstance(day, int)
    assert year >= 0
    assert 1 <= month <= 12
    assert 1 <= day <= 31
    m = calendar.weekday(year, month, day)
    return 'Monday' if m == 0 else 'Tuesday' if m == 1 else 'Wednesday' if m == 2 else 'Thursday' if m == 3 else 'Friday' if m == 4 else 'Saturday' if m == 5 else 'Sunday'
