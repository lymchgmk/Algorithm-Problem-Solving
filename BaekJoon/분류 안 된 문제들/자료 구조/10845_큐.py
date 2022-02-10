import sys
from collections import deque
sys.stdin = open("10845_큐.txt", "rt")


if __name__ == "__main__":
    input = lambda: sys.stdin.readline()
    N = int(input())
    Q = deque()
    for _ in range(N):
        command = input().split()
        if command[0] == "push":
            Q.append(command[1])
        elif command[0] == "pop":
            print(Q.popleft() if Q else -1)
        elif command[0] == "size":
            print(len(Q))
        elif command[0] == "empty":
            print(1 if not Q else 0)
        elif command[0] == "front":
            print(Q[0] if Q else -1)
        elif command[0] == "back":
            print(Q[-1] if Q else -1)
        else:
            continue
