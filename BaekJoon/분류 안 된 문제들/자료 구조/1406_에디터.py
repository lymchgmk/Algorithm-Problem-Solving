import sys
sys.stdin = open("1406_에디터.txt", "rt")


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    stack_l, stack_r = list(input()), []
    M = int(input())
    for _ in range(M):
        command = input().split()
        if command[0] == "L" and stack_l:
            stack_r.append(stack_l.pop())
        elif command[0] == "D" and stack_r:
            stack_l.append(stack_r.pop())
        elif command[0] == "B" and stack_l:
            stack_l.pop()
        elif command[0] == "P":
            stack_l.append(command[1])

    stack_r.reverse()
    print("".join(stack_l + stack_r))

