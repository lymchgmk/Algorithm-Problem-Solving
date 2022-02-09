import sys
sys.stdin = open("9465_스티커.txt", "rt")


def solution(n, stickers):
    for i in range(2, n+1):
        stickers[0][i] = max(stickers[1][i-1], stickers[1][i-2]) + stickers[0][i]
        stickers[1][i] = max(stickers[0][i-1], stickers[0][i-2]) + stickers[1][i]
    return max(stickers[0][-1], stickers[1][-1])


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    T = int(input())
    for _ in range(T):
        n = int(input())
        stickers = [
            [0] + list(map(int, input().split())),
            [0] + list(map(int, input().split()))
        ]
        print(solution(n, stickers))
