import sys
sys.stdin=open("3985_롤 케이크.txt")


L=int(input())
N=int(input())
data=[list(map(int, input().split())) + [i+1] for i in range(N)]

rollcake = [0 for _ in range(L+1)]
for idx, d in enumerate(data):
    for pick in range(d[0], d[1] + 1):
        if rollcake[pick] == 0:
            rollcake[pick] = idx + 1

result = []
audiences = [0 for _ in range(N + 1)]
for idx, cake in enumerate(rollcake):
    if idx != 0 and cake != 0:
        audiences[cake] += 1
    if audiences[cake] != 0:
        result.append([audiences[cake], idx])

hope_longest = sorted(data, key = lambda x : (x[0] - x[1]))[0][2]
take_longest = sorted(enumerate(audiences), key = lambda x : (-x[1], x[0]))