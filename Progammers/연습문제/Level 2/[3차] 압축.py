def solution(msg):
    from collections import deque
    dic = {chr(64+i): i for i in range(1, 27)}
    
    msg = deque(msg)
    last_val = 26
    answer = []
    start = msg.popleft()
    while msg:
        while start in dic:
            start += msg.popleft()
        last_val += 1
        dic[start] = last_val
        answer.append(dic[start[:-1]])
        start = start[-1]
    answer.append(dic[start])
    return answer
    # 1. 없으면 dic에 추가 + 한 칸 줄여서 출력
    # 2. 있으면 계속 늘리기, 없으면 1로

msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))