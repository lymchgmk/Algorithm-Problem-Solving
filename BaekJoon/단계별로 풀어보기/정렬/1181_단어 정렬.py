import sys
sys.stdin = open('1181_단어 정렬.txt', 'rt')


def input():
    return sys.stdin.readline().strip()

N = int(input())
W = sorted(set([input() for _ in range(N)]), key = lambda x: (len(x), x))
for word in W:
    print(word)