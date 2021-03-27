def solution(msg):
    dic = {chr(64+i): i for i in range(1, 27)}
    buffer = ''
    result = []
    for c in msg:
        test = buffer + c
        if test in dic:
            buffer = test
        else:
            result.append(dic[buffer])
            dic[test] = len(dic) + 1
            buffer = c
    
    if buffer:
        result.append(dic[buffer])
    
    return result
            
        
    # 1. 없으면 dic에 추가 + 한 칸 줄여서 출력
    # 2. 있으면 계속 늘리기, 없으면 1로

msg = 'KAKAO'
print(solution(msg))