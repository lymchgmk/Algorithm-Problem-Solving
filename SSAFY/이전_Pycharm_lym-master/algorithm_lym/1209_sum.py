import sys
sys.stdin = open("1209_sum.txt", "r")

def sum_row(list, idx):
    return sum(list[idx])

def sum_column(list, idx):
    column = []
    for i in range(100):
        column.append(list[i][idx])
    return sum(column)

def sum_diagonal(list):
    diagonal = []
    for i in range(100):
        for j in range(100):
            if i == j:
                diagonal.append(list[i][j])
    return sum(diagonal)

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    num = []
    for i in range(100):
        num.append(list(map(int, input().split())))

    max_sum_row = 0
    max_sum_column = 0
    max_sum_diagonal = 0
    if max_sum_diagonal < sum_diagonal(num):
        max_sum_diagonal = sum_diagonal(num)

    for i in range(100):
        if max_sum_row < sum_row(num, i):
            max_sum_row = sum_row(num, i)
        if max_sum_column < sum_column(num, i):
            max_sum_column = sum_column(num, i)

    max_sum_total = max([max_sum_row, max_sum_column, max_sum_diagonal])

    print('#{0} {1}'.format(test_case, max_sum_total))