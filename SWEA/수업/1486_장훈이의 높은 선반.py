import sys
sys.stdin = open("1486_장훈이의 높은 선반.txt")


def powerset(s):
    test_samples = [1 << i for i in range(len(s))]
    for i in range(1 << len(s)):
        yield [ss for ss, sample in zip(s, test_samples) if sample & i]


T=int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    result = float('inf')
    for subset in powerset(H):
        S_sub = sum(subset)

        if B <= S_sub < result:
            result = S_sub

    answer = result - B
    print(f'#{test_case} {answer}')