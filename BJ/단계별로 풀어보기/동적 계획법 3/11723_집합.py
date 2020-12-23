import sys
sys.stdin = open("11723_집합.txt", "rt")
input = lambda: sys.stdin.readline().strip()


M = int(input())
S = []
for _ in range(M):
    temp = input().split()

    if len(temp) == 1:
        oper = temp[0]
        if oper == 'all':
            S = [n for n in range(1, 21)]
        elif oper == 'empty':
            S = []
    
    else:
        oper, x = temp
        x = int(x)
        if oper == 'add':
            if x not in S:
                S.append(x)
        elif oper == 'remove':
            if x in S:
                S.remove(x)
        elif oper == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.append(x)