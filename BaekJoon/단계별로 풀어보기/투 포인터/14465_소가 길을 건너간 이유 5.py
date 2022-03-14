import sys
sys.stdin = open("14465_소가 길을 건너간 이유 5.txt", 'rt')


def solution(N, K, B, arr):
    # 0: 정상 / 1: 고장
    lights = [0] * N
    for a in arr:
        lights[a] = 1
    need_fix = sum(lights[:K])
    ans = need_fix
    left, right = 0, K
    while right < N:
        need_fix -= lights[left]
        need_fix += lights[right]
        ans = min(ans, need_fix)
        left += 1
        right += 1
    print(ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    N, K, B = map(int, input().split())
    arr = [int(input()) - 1 for _ in range(B)]
    solution(N, K, B, arr)
