from datetime import time


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


n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(n, t, m, timetable))
