import sys
sys.stdin = open("6549_히스토그램에서 가장 큰 직사각형.txt", "rt")


input = lambda: sys.stdin.readline().strip()
while True:
    N, *H = list(map(int, input().split()))
    H.append(0)

    if N == 0: break

    stack = []
    answer = 0
    for idx, now_H in enumerate(H):
        while stack and H[stack[-1]] > now_H:
            test_H = H[stack.pop()]
            w = idx - stack[-1] - 1 if stack else idx
            area =  w * test_H
            if answer < area:
                answer = area

        stack.append(idx)

    print(answer)
    