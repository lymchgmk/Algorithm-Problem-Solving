import sys
sys.stdin = open("4843_특별한 정렬.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ai = list(reversed(sorted(list(map(int, input().split())))))

    a = [0] * len(ai)
    ai1 = list(reversed(ai[:int(len(ai) / 2)]))
    ai2 = ai[int(len(ai) / 2):]

    for i in range(len(ai)):
        if i % 2 == 0:
            a[i] = int(ai1.pop())
        else:
            a[i] = int(ai2.pop())

    b = str(a[0:10]).replace(',', '')
    print('#{0} {1}'.format(test_case, b[1:-1]))