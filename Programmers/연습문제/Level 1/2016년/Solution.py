import datetime as dt

def solution(a, b):
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return weekdays[dt.date(2016, a, b).weekday()]
