def solution(num):
    answer = 0
    while num != 1 and answer <= 501:
        print(num)
        if num == 1:
            break

        if not num%2:
            num //= 2
        else:
            num = num*3 + 1
        answer += 1
        
    return answer if answer <= 500 else -1


print(solution(626331))