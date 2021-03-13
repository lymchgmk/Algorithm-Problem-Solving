import sys
sys.stdin = open('2491_수열.txt', 'r')


def ASC(seq):
    n_start = seq[0]
    count = 1
    result = 0
    for n in seq[1:]:
        if n_start <= n:
            count += 1
            n_start = n
        else:
            if result < count:
                result = count
            count, n_start = 1, n
    return max(result, count)


N = int(input())
data = list(map(int, input().split()))

print(max(ASC(data), ASC(data[::-1])))