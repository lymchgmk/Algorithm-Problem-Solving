import sys
sys.stdin = open("1253_좋다.txt", "rt")


def solution(N, A):
    A.sort()

    cnt = 0
    for i in range(N):
        target = A[i]
        _A = A[:i] + A[i+1:]
        left, right = 0, len(_A) - 1
        while left < right:
            _sum = _A[left] + _A[right]
            if _sum == target:
                cnt += 1
                break
            elif _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
    print(cnt)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    A = list(map(int, input().split()))
    solution(N, A)
