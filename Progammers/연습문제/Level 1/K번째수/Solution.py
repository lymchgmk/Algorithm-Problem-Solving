def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = map(lambda x: x-1, command)
        sub_array = sorted(array[i: j+1])
        answer.append(sub_array[k])
    return answer