import sys
sys.stdin = open('2343_기타 레슨.txt', 'rt')


def solution(N, M, L):
    def count_BL(size, L):
        res = 0
        total = 0
        for l in L:
            if total + l <= size:
                total += l
            else:
                total = l
                res += 1
        return res

    left, right = max(L), sum(L)
    ans = left
    while left <= right:
        mid = (left + right) // 2
        cnt = count_BL(mid, L)
        if cnt < M:
            right = mid - 1
        else:
            left = mid + 1
            ans = left
    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    solution(N, M, L)
