import sys

sys.setrecursionlimit(10 ** 6)


def solution(k, room_number):
    def findEmptyRoom(number, rooms):
        if number not in rooms:
            rooms[number] = number + 1
            return number
        else:
            empty = findEmptyRoom(rooms[number], rooms)
            rooms[number] = empty + 1
            return empty
    
    answer = []
    rooms = dict()
    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
    
    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))

