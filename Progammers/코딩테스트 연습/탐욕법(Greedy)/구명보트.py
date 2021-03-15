import collections


def solution(people, limit):
    answer = 0
    people.sort()
    people = collections.deque(people)
    while people:
        weight = people.pop()
        if people and people[0] <= limit - weight:
            people.popleft()
        answer += 1
        
    return answer


people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))