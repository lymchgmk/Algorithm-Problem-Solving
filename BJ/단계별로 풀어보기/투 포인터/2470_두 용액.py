import sys
sys.stdin = open('2470_두 용액.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
sol = list(map(int, input().split()))
sol.sort()

left, right = 0, N-1
target = float('inf')
result_left, result_right = left, right
while left < right:
    tmp = sol[left] + sol[right]
    if abs(tmp) < target:
        result_left, result_right = left, right
        target = abs(tmp)
        if target == 0:
            break
    
    if tmp > 0:
        right -= 1
    else:
        left += 1
    
print(sol[result_left], sol[result_right])
