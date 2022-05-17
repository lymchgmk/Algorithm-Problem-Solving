import re
import collections


def solution(inp_str):
    res = []
    
    # 1
    if not 8 <= (len(inp_str)) <= 15:
        res.append(1)
    
    # 2
    test_group = [0] * 4
    test_1 = re.findall('[A-Z]', inp_str)
    test_2 = re.findall('[a-z]', inp_str)
    test_3 = re.findall('[0-9]', inp_str)
    test_4 = re.findall('[~!@#$%^&*]', inp_str)
    if test_1:
        test_group[0] = 1
    if test_2:
        test_group[1] = 1
    if test_3:
        test_group[2] = 1
    if test_4:
        test_group[3] = 1
    
    if len(test_1) + len(test_2) + len(test_3) + len(test_4) != len(inp_str):
        res.append(2)
    
    # 3
    if sum(test_group) < 3:
        res.append(3)
    
    # 4 & 5
    counter = collections.Counter(inp_str)
    
    # 4
    for key in counter:
        if counter[key] >= 4:
            if re.search(str(key) + '{4,}', inp_str):
                res.append(4)
                break
    
    # 5
    for key in counter:
        if counter[key] >= 5:
            res.append(5)
            break
    
    # 예외 처리
    if not res:
        return [0]
    
    return res



inp_str = "CaCbCgCdC888834A"
print(solution(inp_str))