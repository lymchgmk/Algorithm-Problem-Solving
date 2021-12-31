import sys
sys.stdin = open('1806_부분합.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N, S = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
tmp_sum = 0
min_len = float('inf')

while True:
    if tmp_sum >= S:
        min_len = min(min_len, right - left)
        tmp_sum -= nums[left]
        left += 1
    
    elif right == N:
        break
    
    else:
        tmp_sum += nums[right]
        right += 1

print(min_len if min_len != float('inf') else 0)
