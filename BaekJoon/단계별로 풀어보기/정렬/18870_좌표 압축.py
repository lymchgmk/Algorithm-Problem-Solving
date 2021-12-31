import sys
sys.stdin = open('18870_좌표 압축.txt', 'rt')


input = lambda:sys.stdin.readline().strip()
N = int(input())
X = list(map(int, input().split()))
sorted_set_X = list(sorted(set(X)))
dict_sorted_set_X = {sorted_set_X[i]: i for i in range(len(sorted_set_X))}
print(*[dict_sorted_set_X[x] for x in X])