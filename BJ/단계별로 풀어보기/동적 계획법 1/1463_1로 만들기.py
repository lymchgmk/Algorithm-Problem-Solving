import sys
sys.stdin = open("1463_1로 만들기.txt", 'rt')


X = int(input())
dp = [1]
cnt = 0
while X not in dp:
    temp = set()
    cnt += 1
    for d in dp:
        if 3*d == X or 2*d == X or d+1 == X:
            print(cnt)
            sys.exit()
        else:
            if 3*d < X:
                temp.add(3*d)
            if 2*d < X:
                temp.add(2*d)
            if d+1 < X:
                temp.add(d+1)
    dp = temp
print(cnt)


'''
def f(n):
    if n < 2:
        return 
    else: 
        min(f(n//i) + n%i + 1 for i in (2,3))

print(f(int(input())))
'''