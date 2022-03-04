import sys
sys.stdin = open('2512_예산.txt', 'rt')


def solution(N, budgets, M):
    max_budget = max(budgets)
    sum_budget = sum(budgets)
    # 다 예산 배정 가능한 경우
    if sum_budget <= M:
        print(max_budget)
    # 불가능한 경우
    else:
        start, end = 0, max_budget
        ans = max_budget
        while start <= end:
            mid = (start + end) // 2
            _total_budget = sum([min(budget, mid) for budget in budgets])
            if _total_budget <= M:
                start = mid + 1
                ans = start
            else:
                end = mid - 1
        print(end)


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    budgets = list(map(int, input().split()))
    M = int(input())
    solution(N, budgets, M)
