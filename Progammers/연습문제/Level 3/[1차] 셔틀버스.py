from datetime import time, timedelta


def solution(n, t, m, timetable):
    answer = ''
    td = timedelta(minutes=t)
    print(list(bus))
    for ttb in timetable:
        h, m = map(int, ttb.split(':'))
        tm = time(hour=h, minute=m)
    return answer


n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))
