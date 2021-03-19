def solution(a, b):
    import datetime
    weekday = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    dt = datetime.date(2016, a, b)
    return weekday[dt.weekday()]

a = 5
b = 24
print(solution(a, b))