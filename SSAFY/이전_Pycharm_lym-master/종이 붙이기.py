import sys
sys.stdin = open("종이 붙이기.txt", "r")

def paper_odd(num):
    if num == 1:
        return 1
    else:
        return 4*paper_odd(num-1) + 1

def paper_even(num):
    if num == 1:
        return 3
    else:
        return int((paper_odd(num)-1)/2) +1


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    odd_or_even = N//10
    num = odd_or_even//2 + 1

    if odd_or_even % 2 == 1:
        print("#{0} {1}".format(test_case, paper_odd(num)))
    else:
        print("#{0} {1}".format(test_case, paper_even(num)))