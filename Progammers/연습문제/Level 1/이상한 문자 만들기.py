def solution(s):
    answer = ''
    tmp = []
    idx = 0
    for char in s:
        if char == ' ':
            idx = 0
            tmp.append([idx, char])
        else:
            tmp.append([idx, char])
            idx += 1
    
    print(tmp)
    for idx, char in tmp:
        if not idx % 2:
            answer += char.upper()
        else:
            answer += char.lower()
    
    return answer


s = "try hello  world "
print(solution(s))