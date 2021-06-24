import sys
sys.stdin = open("(6190)정곤이의단조증가하는수_input.txt")

def solve(x):  #123
    t = x % 10  # 3
    x //= 10    # 12
    while x:
       if x % 10 > t:   # 2 > 3
           return False
       t = x % 10
       x //= 10

    return True

T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    rst = -1
    for i in range(N):
        for j in range(i+1, N):
            num = data[i] * data[j]
            if solve(num):
               if rst < num : rst = num

    print("#{} {}".format(tc+1, rst))
