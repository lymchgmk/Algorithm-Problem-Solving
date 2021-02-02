import sys
sys.stdin = open("2629_양팔저울.txt", "rt")
input = lambda: sys.stdin.readline().strip()


s = int(input())
sinkers = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

measurable = []
is_measured = [[0]*40001 for _ in range(s+1)]

def knapsack(sinkers, s, now, left, right, measurable):
    measured = abs(left - right)
    if measured not in measurable:
        measurable.append(measured)
    
    if now == s:
        return 0
    
    if is_measured[now][measured] == 0:
        sinker = sinkers[now]
        # left
        knapsack(sinkers, s, now+1, left + sinker, right, measurable)

        # right
        knapsack(sinkers, s, now+1, left, right + sinker, measurable)

        # no
        knapsack(sinkers, s, now+1, left, right, measurable)

        is_measured[now][measured] = 1


knapsack(sinkers, s, 0, 0, 0, measurable)

ans = []
for marble in marbles:
    if marble in measurable:
        ans.append('Y')
    else:
        ans.append('N')
print(*ans)