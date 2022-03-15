import sys
sys.stdin = open("2473_세 용액.txt", "rt")


def solution(N, A):
    A.sort()
    res = float('inf')
    ans = [0, 0, 0]
    for i in range(N-2):
        left, right = i+1, N-1
        while left < right:
            _sum = A[i] + A[left] + A[right]
            if res > abs(_sum):
                ans = [A[i], A[left], A[right]]
                res = abs(_sum)

            if _sum == 0:
                print(A[i], A[left], A[right])
                break
            elif _sum < 0:
                left += 1
            else:
                right -= 1
    print(*ans)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    A = list(map(int, input().split()))
    solution(N, A)
