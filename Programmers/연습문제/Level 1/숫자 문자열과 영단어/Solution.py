def solution(s):
    nums_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = ""
    substr = ""
    for char in s:
        if char.isdigit():
            answer += char
        else:
            substr += char
        
        if substr in nums_dict:
            answer += str(nums_dict[substr])
            substr = ""
    return int(answer)
