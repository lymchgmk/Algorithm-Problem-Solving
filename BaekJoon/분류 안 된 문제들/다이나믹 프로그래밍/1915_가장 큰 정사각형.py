import sys
sys.stdin = open("1915_가장 큰 정사각형.txt", "rt")


def solution(n, m, arr):
    answer = max(max(arr))
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j]:
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1
                answer = max(answer, arr[i][j])
    return answer**2


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    n, m = map(int, input().split())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    print(solution(n, m, arr))
