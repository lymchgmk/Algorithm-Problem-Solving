def solution(s):
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    answer = s
    for key, val in num_dict.items():
        answer = answer.replace(key, val)
    return int(answer)


s = "23four5six7"
print(solution(s))