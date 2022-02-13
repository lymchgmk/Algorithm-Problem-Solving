import sys
sys.stdin = open("9466_텀 프로젝트.txt", 'rt')


def solution(n, s):
    res = 0
    for root in range(1, n+1):
        stack = [root]
        team = [root]
        while stack:
            curr = stack.pop()
            post = s[curr]
            if post == root:
                res += 1
                break
            else:
                if post == curr:
                    break
                else:
                    stack.append(post)
                    team.append(post)
    return n - res


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = [0] + list(map(int, input().split()))
        print(solution(n, s))