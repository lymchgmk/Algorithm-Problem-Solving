import sys
sys.stdin = open('9012_괄호.txt', 'rt')


N = int(input())
for _ in range(N):
    stack = []
    flag = True
    PS = sys.stdin.readline().strip()
    for i in range(len(PS)):
        if PS[i] == '(':
            stack.append(PS[i])
        else:
            if not stack:
                flag = False
                break
            else:
                stack.pop()

    if not stack and flag == True:
        print('YES')
    else:
        print('NO')
    