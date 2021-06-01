array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def my_solution(array, commands):
    return [sorted(array[command[0]-1: command[1]])[command[2]-1] for command in commands]

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(solution(array, commands))