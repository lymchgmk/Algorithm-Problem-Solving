import sys
sys.stdin = open('13322_접두사 배열.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


S = input()
prefix_array = [idx for idx in range(len(S))]
for prefix in prefix_array:
    print(prefix)