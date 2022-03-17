import sys
sys.stdin = open("9466_텀 프로젝트.txt", 'rt')


def solution(n, s):
    def dfs(node):
        nonlocal visited
        stack = []
        check = set()
        while not visited[node]:
            stack.append(node)
            check.add(node)
            visited[node] = True
            node = s[node]
        return node, stack, check

    def grouped_check(node, stack, check):
        nonlocal grouped, answer
        if node in check:
            while stack:
                curr = stack.pop()
                if not grouped[curr]:
                    grouped[curr] = True
                    answer -= 1
                if curr == node:
                    break

    visited, grouped = [False] * n, [False] * n
    answer = n
    for i in range(n):
        if not visited[i]:
            node, stack, check = dfs(i)
            grouped_check(node, stack, check)
    print(answer)


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = list(map(lambda x: int(x)-1, input().split()))
        solution(n, s)
