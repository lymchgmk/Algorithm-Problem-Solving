import sys
sys.stdin = open('2004_조합 0의 개수.txt', 'rt')


def count_power(num, div):
    count = 0
    div_n = div
    while num >= div_n:
        count += num // div_n
        div_n *= div
    return count


n, m = map(int, input().split())

count_power_2 = count_power(n, 2) - count_power(m, 2) - count_power(n-m, 2)
count_power_5 = count_power(n, 5) - count_power(m, 5) - count_power(n-m, 5)
print(min(count_power_2, count_power_5))