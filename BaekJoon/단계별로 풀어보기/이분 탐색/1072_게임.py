import sys
sys.stdin = open('1072_게임.txt', 'rt')


def solution(X, Y):
    def calc_Z(X, Y):
        return (Y * 100) // X

    Z = calc_Z(X, Y)
    if Z >= 99:
        print(-1)
    else:
        start, end = 1, X
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            if calc_Z(X + mid, Y + mid) <= Z:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    X, Y = map(int, input().split())
    solution(X, Y)
