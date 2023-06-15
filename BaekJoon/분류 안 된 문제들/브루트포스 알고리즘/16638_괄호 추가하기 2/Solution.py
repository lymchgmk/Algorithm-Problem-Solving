import sys
sys.stdin = open("input.txt", "rt")


def dfs(op_idx, brackets):
    global answer

    if len(ops) <= op_idx:
        exp_stack = [nums[0]]
        for idx, isBracket in enumerate(brackets):
            if isBracket:
                exp_stack.extend(['(', exp_stack.pop(), ops[idx], nums[idx + 1], ')'])
            else:
                exp_stack.extend([ops[idx], nums[idx + 1]])

        result_exp = ''.join(exp_stack)
        answer = max(answer, eval(result_exp))
        return

    tmp1_brackets = brackets.copy()
    dfs(op_idx + 1, tmp1_brackets)

    tmp2_brackets = brackets.copy()
    tmp2_brackets[op_idx] = True
    dfs(op_idx + 2, tmp2_brackets)

    if op_idx + 2 < len(ops):
        tmp3_brackets = brackets.copy()
        tmp3_brackets[op_idx + 1] = True
        dfs(op_idx + 3, tmp3_brackets)


if __name__ == "__main__":
    input = lambda: sys.stdin.readline().strip()
    N = int(input())
    exp = input()
    nums, ops = [], []
    for e in exp:
        nums.append(e) if e.isdigit() else ops.append(e)

    answer = float('-inf')

    brackets = [False] * len(ops)
    dfs(0, brackets)
    print(answer)
