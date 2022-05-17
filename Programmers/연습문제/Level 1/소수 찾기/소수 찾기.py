def solution(n):
    num=set(range(2,n+1))
    for i in range(2,n+1):
        num-=set(range(2*i,n+1,i))
    return len(num)



n = 10
answer = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        answer.append(i)
print(len(answer))