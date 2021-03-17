def solution(begin, end):
    answer = [0]*(end-begin+1)
    for i in range(begin, end+1):
        for j in range(int(i**0.5)+1, 0, -1):
            if i%j == 0:
                answer[i-begin] = j
                break
    return answer



begin = 1
end = 10
print(solution(begin, end))