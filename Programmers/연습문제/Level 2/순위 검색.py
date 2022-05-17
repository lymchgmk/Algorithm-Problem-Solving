def solution(info, query):
    from itertools import product
    from collections import defaultdict
    import re
    import bisect
    
    info_dict = defaultdict(list)
    for i in info:
        language, position, carrer, soulfood, point = i.split()
        _keys = (('-', language), ('-', position), ('-', carrer), ('-', soulfood))
        for key in product(*_keys):
            info_dict[key].append(int(point))
    
    for val in info_dict.values():
        val.sort()
    
    answer = []
    for q in query:
        *key, lower_bound = re.findall(r'[-]|\b(?!and\b)\w+', q)
        key, lower_bound = tuple(key), int(lower_bound)
        points = info_dict[key]
        over_lower_bound = len(points) - bisect.bisect_left(points, lower_bound)
        answer.append(over_lower_bound)
    
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
