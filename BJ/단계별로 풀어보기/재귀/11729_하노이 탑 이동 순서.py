import sys
sys.stdin = open('11729_하노이 탑 이동 순서.txt', 'rt')


def hanoi(n, a, b, c):
    global answer
    if n == 1:
        answer.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        answer.append([a, c])
        hanoi(n-1, b, a, c)


N = int(input())
answer = []
hanoi(N, 1, 2, 3)
print(2**N - 1)
for ans in answer:
    print(*ans)
