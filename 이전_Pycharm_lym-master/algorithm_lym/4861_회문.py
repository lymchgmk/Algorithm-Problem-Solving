import sys
sys.stdin = open("4861_회문.txt", "r")

def palindrome(list, K):
    for i in range(len(list)-K+1):
        sample_list = list[i:i+K]
        if sample_list == sample_list[::-1]:
            return sample_list

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    NN = []

    for i in range(N):
        NN.append(list(str(input())))

    for i in range(N):
        row = NN[i]
        column = [row[i] for row in NN]

        if palindrome(row, M) is not None:
            p_row = ''.join(palindrome(row, M))
            print("#{0} {1}".format(test_case, p_row))

        if palindrome(column, M) is not None:
            p_column = ''.join(palindrome(column, M))
            print("#{0} {1}".format(test_case, p_column))

