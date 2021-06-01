import collections


def solution(priorities, location):
    answer = 0
    deq = collections.deque(enumerate(priorities))
    while deq:
        temp = deq.popleft()
        for doc in deq:
            if temp[1] < doc[1]:
                deq.append(temp)
                break
        else:
            answer += 1
            if temp[0] == location:
                break
    return answer
    
    

priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))