# Task description: With the help of id, assign task to the id in the weekdays of the month
import calendar

import _datetime
import sys



ids = ['1', '2', '3', '4', '5']

def pickId():
    print(sys.argv)
    print('hello')


def date_iter(year, month):
    cal = calendar.Calendar()


    for day in cal.iterweekdays():
        print(calendar.day_name[day])

    for d in cal.itermonthdates(2022,9):
        print(d)
    
    
"""
def get_all_days(mon):
    

     return ['{:04d}-{:02d}-{:02d}'.format(y, m, d) for d in range(1, monthrange(y, m, d)[1] + 1)]
"""
pickId()
date_iter(2022,9)


#print(get_all_days('Sept, 2022'))
