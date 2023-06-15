import sys
sys.stdin = open("input.txt", "rt")


def dfs(idx, sub_total):
    global answer

    print(idx, sub_total)

    if idx == len(ops):
        answer = max(answer, int(sub_total))
        return

    first = str(eval(sub_total + ops[idx] + nums[idx + 1]))
    dfs(idx + 1, first)

    if idx + 1 < len(ops):
        second = str(eval(nums[idx + 1] + ops[idx + 1] + nums[idx + 2]))
        second = str(eval(sub_total + ops[idx] + second))
        dfs(idx + 2, second)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    exp = input()
    nums, ops = [], []
    for e in exp:
        nums.append(e) if e.isdigit() else ops.append(e)
    # result = 9
    answer = float('-inf')
    dfs(0, nums[0])
    print(answer)
