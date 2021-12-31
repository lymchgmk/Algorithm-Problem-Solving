import sys
sys.stdin = open('5430_AC.txt', 'rt')


from collections import deque


input = lambda: sys.stdin.readline().strip()
T = int(input())
for _ in range(T):
    P = input()
    N = int(input())
    X = input().replace('[', '').replace(']', '').split(',')
    if X == ['']:
        X = deque()
    else:
        X = deque(list(map(int, X)))

    rev_flag = False
    for p in P:
        if p == "R":
            rev_flag = not rev_flag
        elif p == "D":
            if not X:
                print('error')
                break
            
            if rev_flag == True:
                X.pop()
            else:
                X.popleft()
    
    else:
        if rev_flag:
            X = list(X)[::-1]
        else:
            X = list(X)
        print(str(X).replace(' ', ''))
