from datetime import datetime, time, timedelta


def solution(n, t, m, timetable):
    answer = ''
    buses = [[time(hour=9).replace(hour=9+(t*i//60), minute=(t*i) % 60), n] for i in range(n)]
    timetable.sort()
    crews = [time.fromisoformat(ttb) for ttb in timetable]
    print('crews', crews)
    print('buses', buses)
    
    for crew in crews:
        for bus in buses:
            if bus[0] >= crew:
                bus[1] -= 1
                break
    
    print(buses)
    
    return answer


n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))
