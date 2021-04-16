from collections import deque


def solution(s):
    def is_correct(deq):
        stack = []
        bracket_dict = {')':'(', ']':'[', '}':'{'}
        for bracket in deq:
            if bracket in ('(', '[', '{'):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                elif stack[-1] == bracket_dict[bracket]:
                    stack.pop()
        return not stack
    
    deq_s = deque(s)
    answer = 0
    for _ in range(len(s)):
        deq_s.rotate(-1)
        if is_correct(deq_s):
            answer += 1
    return answer


s = "[](){}"
print(solution(s))
