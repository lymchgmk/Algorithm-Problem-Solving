import sys
sys.stdin = open("4837_부분집합의 합.txt", "r")


def powerset_NK(s, n, k):
    count = 0
    for i in range(1 << len(s)):
        subset = [s[j] for j in range(len(s)) if i & (1 << j)]
        if len(subset) == n and sum(subset) == k:
            count += 1
    return count


T = int(input())
A = list(range(1, 13))

for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    print("#{0} {1}".format(test_case, powerset_NK(A, N, K)))