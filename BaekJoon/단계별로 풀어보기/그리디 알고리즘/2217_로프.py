import sys
sys.stdin = open('2217_로프.txt', 'rt')


def solution(N, lopes):
    lopes.sort(reverse=True)
    ans = 0
    for idx, lope in enumerate(lopes, start=1):
        ans = max(ans, idx * lope)
    print(ans)
    

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    lopes = [int(input()) for _ in range(N)]
    solution(N, lopes)
