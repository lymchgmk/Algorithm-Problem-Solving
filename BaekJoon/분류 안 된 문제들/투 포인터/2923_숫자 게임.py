import sys
import os
from collections import Counter
file_name = os.path.basename(sys.argv[0])[:-3] + ".txt"
sys.stdin = open(file_name, "rt")


if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    A_cntr, B_cntr = Counter(), Counter()
    for _ in range(N):
        A, B = map(int, input().split())
        A_cntr[A] += 1
        B_cntr[B] += 1

        cntr_A, cntr_B = A_cntr.copy(), B_cntr.copy()
        num_A, num_B = 1, 100
        answer = 0
        while 1 <= num_A <= 100 and 1 <= num_B <= 100:
            if cntr_A[num_A] and cntr_B[num_B]:
                cand = num_A + num_B
                if answer < cand:
                    answer = cand

                if cntr_A[num_A] < cntr_B[num_B]:
                    cntr_B[num_B] -= cntr_A[num_A]
                    cntr_A[num_A] = 0
                    num_A += 1
                elif cntr_A[num_A] > cntr_B[num_B]:
                    cntr_A[num_A] -= cntr_B[num_B]
                    cntr_B[num_B] = 0
                    num_B -= 1
                else:
                    cntr_A[num_A] = cntr_B[num_B] = 0
                    num_A += 1
                    num_B -= 1
            else:
                num_A += not cntr_A[num_A]
                num_B -= not cntr_B[num_B]
        print(answer)
