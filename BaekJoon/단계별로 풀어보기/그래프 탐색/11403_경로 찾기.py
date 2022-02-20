import sys
sys.stdin = open("11403_경로 찾기.txt", "rt")


def solution(N, adj):
    answer = [[0]*N for _ in range(N)]
    for start in range(N):
        stack = [start]
        while stack:
            curr = stack.pop()
            for post, can_go in enumerate(adj[curr]):
                if can_go and answer[start][post] == 0:
                    answer[start][post] = 1
                    stack.append(post)
    for ans in answer:
        print(*ans)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    solution(N, adj)
