from collections import deque


def solution(s):
    def is_correct(deq):
        stack = []
        chk_dict = {')': '(', ']': '[', '}': '{'}
        for bracket in deq:
            if bracket in ('(', '[', '{'):
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == chk_dict[bracket]:
                        stack.pop()

        return not stack
    
    answer = 0
    deq_s = deque(s)
    for _ in range(len(s)):
        deq_s.rotate(-1)
        if is_correct(deq_s):
            answer += 1
    return answer


s = "}]()[{"
print(solution(s))