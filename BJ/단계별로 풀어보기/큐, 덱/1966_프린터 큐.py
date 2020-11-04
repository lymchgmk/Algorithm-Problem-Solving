import sys
sys.stdin = open('1966_프린터 큐.txt', 'rt')


from collections import deque


test_case = int(input())
for _ in range(test_case):
    N, M = map(int, input().split())
    deq = deque(enumerate(list(map(int, input().split()))))
    printed = False
    count = 1
    print("deq", deq)
    while deq:
        for i in range(N):
            if deq[0][1] < deq[i][1]:
                deq.append(deq.popleft())
                break
        else:
            print(deq)
            if deq[0][0] == M:
                print(count)
                break
            else:
                deq.popleft()
                count += 1




            
