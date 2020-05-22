def solution(k, room_number):
    answer = []
    rooms=dict()

    for i in range(1, k+1):
        rooms.setdefault(i, 0)
        print(rooms)

    return answer

    solution(10, 5)
