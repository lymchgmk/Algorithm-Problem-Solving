from datetime import datetime, time, timedelta


def solution(n, t, m, timetable):
    answer = ''
    buses = [[datetime(2000, 1, 1, 9, 0, 0) + timedelta(minutes=t)*i, n] for i in range(n)]
    crews = [time(*map(int, ttb.split(':'))) for ttb in timetable]
    crews.sort()
    
    print(buses)
    
    return answer


n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))
