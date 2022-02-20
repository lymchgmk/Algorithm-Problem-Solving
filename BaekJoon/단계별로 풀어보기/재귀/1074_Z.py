import sys
sys.stdin = open("1074_Z.txt", "rt")
sys.setrecursionlimit(10**9)


def solution(N, r, c):
    def recursion(SIZE, start_r, start_c):
        nonlocal dirs, cnt
        if SIZE == 2:
            for d_r, d_c in dirs:
                if start_r + d_r == r and start_c + d_c == c:
                    return
                cnt += 1

        for next_r in range(start_r, start_r + SIZE, SIZE // 2):
            for next_c in range(start_c, start_c + SIZE, SIZE // 2):
                if next_r <= r < next_r + SIZE // 2 and next_c <= c < next_c + SIZE // 2:
                    recursion(SIZE // 2, next_r, next_c)
                    return
                cnt += SIZE ** 2 // 4

    SIZE = 2**N
    dirs = ((0, 0), (0, 1), (1, 0), (1, 1))
    cnt = 0
    recursion(SIZE, 0, 0)
    print(cnt)


if __name__ == "__main__":
    N, r, c = map(int, input().split())
    solution(N, r, c)
