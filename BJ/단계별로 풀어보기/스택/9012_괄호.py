import sys
sys.stdin = open('9012_괄호.txt', 'rt')


N = int(input())
stack = []
for _ in range(N):
    flag = True
    PS = sys.stdin.readline().strip()
    for i in range(len(PS)):
        if PS[i] == '(':
            stack.append(PS[i])
        else:
            try:
                stack.pop()
            except:
                flag = False
                break
    if not stack and flag == True:
        print('YES')
    else:
        print('NO')
    