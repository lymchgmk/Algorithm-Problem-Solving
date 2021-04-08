import datetime as dt


def solution(n, t, m, timetable):
    buses = [[dt.time(hour=9).replace(hour=9+(t*i//60), minute=(t*i) % 60), m, []] for i in range(n)]
    timetable.sort()
    crews = [dt.time.fromisoformat(tmtb) if tmtb != '24:00' else dt.time(hour=0, minute=0) for tmtb in timetable]
    for idx, crew in enumerate(crews):
        for bus in buses:
            if bus[1] > 0 and bus[0] >= crew:
                bus[1] -= 1
                bus[2].append(idx)
                break
                
    # 마지막 버스에 자리가 있다 / 없다
    if buses[-1][1] == 0:
        last_ride_crew = buses[-1][2][-1]
        tmp = crews[last_ride_crew].isoformat()
        
        tmp_h, tmp_m, _ = map(int, tmp.split(':'))
        if tmp_m == 0:
            tmp_h, tmp_m = tmp_h-1, 59
        else:
            tmp_m -= 1
        answer = dt.time(hour=tmp_h, minute=tmp_m).isoformat()[:-3]
    else:
        answer = buses[-1][0].isoformat()[:-3]
    
    return answer
    

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))
