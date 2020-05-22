import sys
sys.stdin=open("5188_최소합.txt")

def route(i, j, result):
    global answer
    if result > answer:
        return
    if i >= N or j >= N:
        return
    elif [i, j] == [N - 1, N - 1]:
        result += NxN[i][j]
        if answer > result:
            answer = result
        return
    else:
        result += NxN[i][j]

        route(i + 1, j, result)
        route(i, j + 1, result)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    NxN = [list(map(int, input().split())) for _ in range(N)]

    result, answer = 0, 10000

    route(0,0,0)
    print("#{} {}".format(test_case, answer))