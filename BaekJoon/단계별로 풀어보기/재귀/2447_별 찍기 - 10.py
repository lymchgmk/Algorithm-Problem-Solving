import sys
sys.stdin = open('2447_별 찍기 - 10.txt', 'rt')


def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix
 
 
star = ["***", "* *", "***"]
N = int(input())
k = 0

while N != 3:
    N //= 3
    k += 1

for i in range(k):
    star = get_stars(star)

for i in star:
    print(i)
