def solution(enter, leave):
    answer = [0] * len(enter)
    room = set()
    e_idx = 0
    for l in leave:
        while l not in room:
            room.add(enter[e_idx])
            e_idx += 1

        room.discard(l)
        for man in room:
            answer[man-1] += 1
        answer[l-1] += len(room)
    return answer


if __name__ == "__main__":
    enter = [3, 2, 1]
    leave = [1, 3, 2]
    print(solution(enter, leave))