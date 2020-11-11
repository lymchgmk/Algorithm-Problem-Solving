import sys
sys.stdin = open('1966_프린터 큐.txt', 'rt')


from collections import deque


test_case = int(input())
for _ in range(test_case):
    N, M = map(int, input().split())
    deq = deque(enumerate(list(map(int, input().split()))))
    cnt = 0
    while deq:
        test = deq.popleft()
        for d in deq:
            if d[1] > test[1]:
                deq.append(test)
                break
        else:
            cnt += 1
            if test[0] == M:
                break
    print(cnt)




            
