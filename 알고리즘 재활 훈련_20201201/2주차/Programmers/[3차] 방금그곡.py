import sys


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def solution(m, musicinfos):
    answer = ''
    result = []

    for musicinfo in musicinfos:
        idx = 1
        start, end, title, music = musicinfo.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = (end_h - start_h)*60 + (end_m - start_m)
        radio = (music*(time//len(music)+2))
        if radio[time+1] == '#':
            radio = radio[:time+1]
        else:
            radio = radio[:time]
        
        if len(radio) < len(m):
            continue

        for i in range(len(radio)-len(m)+1):
            for j in range(len(m)):
                if radio[i+j] != m[j]:
                    break
            else:
                result.append([time, idx, title])
        idx += 1
    
    if not result:
        return None
    else:
        return sorted(result, key=lambda x: (-x[0], x[1]))[0][2]


print(solution(m, musicinfos))