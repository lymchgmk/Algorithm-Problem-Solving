import sys
sys.stdin = open('16637_괄호추가하기.txt')


def dfs(idx, sub_total):
    print(sub_total)
    global answer
    
    if idx == len(ops):
        answer = max(answer, int(sub_total))
        return
    
    first = str(eval(sub_total + ops[idx] + nums[idx+1]))
    dfs(idx+1, first)
    
    if idx+1 < len(ops):
        second = str(eval(nums[idx+1] + ops[idx+1] + nums[idx+2]))
        second = str(eval(sub_total + ops[idx] + second))
        dfs(idx+2, second)


input = lambda: sys.stdin.readline().strip()
N = int(input())
expression = input()
nums, ops = [], []
for e in expression:
    nums.append(e) if e.isdigit() else ops.append(e)

answer = float('-inf')

dfs(0, nums[0])

print(answer)
