import sys
sys.stdin = open("14889_스타트와 링크.txt", "rt")


def start_link(idx, cnt):
    global ans
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if is_picked[i] and is_picked[j]:
                    start += S[i][j]
                elif not is_picked[i] and not is_picked[j]:
                    link += S[i][j]
        ans = min(ans, abs(start - link))
    
    else:
        for i in range(idx, N):
            if is_picked[i]:
                continue
            else:
                is_picked[i] = True
                start_link(i+1, cnt+1)
                is_picked[i] = False


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input().strip())
    S = [list(map(int, input().strip().split())) for _ in range(N)]
    is_picked = [False] * N
    ans = float('inf')
    start_link(0, 0)
    print(ans)