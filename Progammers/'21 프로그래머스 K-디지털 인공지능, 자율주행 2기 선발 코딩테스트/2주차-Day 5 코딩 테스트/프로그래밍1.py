from collections import deque


def solution(n, signs):
    def _can_ride(start, sign):
        return deque([(start, dest) for dest, can_ride in enumerate(sign) if can_ride])
    
    answer = [[0] * n for _ in range(n)]
    for start, sign in enumerate(signs):
        deq = _can_ride(start, sign)
        while deq:
            curr, dest = deq.popleft()
            if answer[curr][dest] == 0:
                deq.extend(_can_ride(start, signs[dest]))
                answer[curr][dest] = 1
    
    return answer