import sys
sys.stdin = open("5658_보물상자.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num = list(str(input()))
    cut = int(len(num) / 4)

    rotate = 0
    n_list = []
    while rotate < cut:
        n1 = ''.join(num[:cut])
        n2 = ''.join(num[cut:2 * cut])
        n3 = ''.join(num[2 * cut:3 * cut])
        n4 = ''.join(num[3 * cut:])
        n_list.extend([n1, n2, n3, n4])

        num.append(num[0])
        del num[0]

        rotate += 1

    n_list = list(set(n_list))
    sorted_n_list = sorted(n_list, reverse = True)

    ans = int(sorted_n_list[K-1], 16)

    print('#{0} {1}'.format(test_case, ans))


