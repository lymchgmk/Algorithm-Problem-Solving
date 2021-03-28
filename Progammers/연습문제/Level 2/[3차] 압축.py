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

msg = 'KAKAO'
print(solution(msg))