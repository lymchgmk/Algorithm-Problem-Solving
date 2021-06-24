import sys
sys.stdin = open("4839_이진탐색.txt", "r")

def bs_book(p, key):
    start = 1
    end = p
    count = 1
    if key == int((start+end)/2):
        return count
    while True:
        count += 1
        middle = int((start+end)/2)
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
    return count

T = int(input())
A = list(range(1, 13))

for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())

    if bs_book(P, Pa) < bs_book(P, Pb):
        print("#{0} {1}".format(test_case, "A"))
    elif bs_book(P, Pa) > bs_book(P, Pb):
        print("#{0} {1}".format(test_case, "B"))
    else:
        print("#{0} {1}".format(test_case, 0))