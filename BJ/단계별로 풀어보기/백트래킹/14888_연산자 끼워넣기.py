import sys
sys.stdin = open("14888_연산자 끼워넣기.txt", "rt")

'''
from itertools import permutations
from collections import deque
import copy


def solve_with_permutation(n, num_list, operation_count_list):
    op = ['+', '-', '*', '//']
    operation_list = []
    max, min = -(sys.maxsize + 1), sys.maxsize
    for i in range(4):
        temp = [op[i]] * operation_count_list[i]
        operation_list.extend(temp)
    
    case_list = set(permutations(operation_list, n-1))
    for case in case_list:
        temp_list = deque(copy.deepcopy(num_list))
        idx = -1
        result = temp_list.popleft()
        while temp_list:
            idx += 1
            next_num = temp_list.popleft()
            current_op = case[idx]

            if current_op == '+':
                result += next_num
            elif current_op == '-':
                result -= next_num
            elif current_op == '*':
                result *= next_num
            else:
                if result < 0:
                    result *= (-1)
                    result //= next_num
                    result *= (-1)
                else:
                    result //= next_num
        
        if result < min:
            min = result
        if result > max:
            max = result
    
    return max, min


if __name__ == "__main__":
    N = int(input())
    A = deque(list(map(int, sys.stdin.readline().split())))
    op_cnt_list = deque(list(map(int, sys.stdin.readline().split())))
    
    max, min = solve_with_permutation(N, A, op_cnt_list)
    print(max)
    print(min)
'''


input = sys.stdin.readline

def cal(num, idx, add, sub, mul, div):
    global N, max_v, min_v
    if idx == N:
        max_v, min_v = max(num, max_v), min(num, min_v)
        return
    else:
        if add:
            cal(num + num_list[idx], idx + 1, add - 1, sub, mul, div)
        if sub:
            cal(num - num_list[idx], idx + 1, add, sub - 1, mul, div)
        if mul:
            cal(num * num_list[idx], idx + 1, add, sub, mul - 1, div)
        if div:
            cal(int(num / num_list[idx]), idx + 1, add, sub, mul, div - 1)


if __name__ == "__main__":
    max_v, min_v = -(sys.maxsize+1), sys.maxsize
    N = int(input())
    num_list = list(map(int, input().strip().split()))
    add, sub, mul, div = map(int, input().strip().split())
    cal(num_list[0], 1, add, sub, mul, div)

    print(max_v)
    print(min_v)