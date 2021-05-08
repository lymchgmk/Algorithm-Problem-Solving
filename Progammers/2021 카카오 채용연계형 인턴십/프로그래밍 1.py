def solution(s):
    nums_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    res = []
    sub_s = ''
    for char in s:
        if char.isdigit():
            res.append(char)
        else:
            sub_s += char
            if sub_s in nums_dict:
                res.append(nums_dict[sub_s])
                sub_s = ''
    
    return int(''.join(res))


s = "one4seveneight"
print(solution(s))
