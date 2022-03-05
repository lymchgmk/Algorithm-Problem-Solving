import sys
sys.stdin = open('1535_안녕.txt', 'rt')


def solution(N, hp, happy):
    knapsack = [[0]*101 for _ in range(101)]
    for i in range(1, N+1):
        for j in range(100):
            if j < hp[i-1]:
                knapsack[i][j] = knapsack[i-1][j]
            else:
                knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-hp[i-1]] + happy[i-1])
    return knapsack[N][99]


if __name__ == "__main__":
    N = int(input())
    hp = list(map(int, input().split()))
    happy = list(map(int, input().split()))
    print(solution(N, hp, happy))