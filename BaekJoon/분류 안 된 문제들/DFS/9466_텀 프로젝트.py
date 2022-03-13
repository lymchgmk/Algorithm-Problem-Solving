import sys
sys.stdin = open("9466_텀 프로젝트.txt", 'rt')


def solution(n, s):
    def check_group(start):
        nonlocal is_grouped, group_failed
        group = set()
        curr = start
        while curr not in group:
            if is_grouped[curr] or group_failed[curr]:
                return
            group.add(curr)
            curr = s[curr]

        if start == curr:
            for student in group:
                is_grouped[student] = True
        else:
            group.remove(curr)
            for student in group:
                group_failed[student] = True

    is_grouped = [False] * n
    group_failed = [False] * n
    for start in range(n):
        if not is_grouped[start]:
            check_group(start)

    print(n - sum(is_grouped))


if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = list(map(lambda x: int(x)-1, input().split()))
        solution(n, s)
