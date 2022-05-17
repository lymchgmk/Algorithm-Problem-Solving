import collections


def solution(table, languages, preference):
    l_per_p = {l: p for l, p in zip(languages, preference)}
    res = collections.defaultdict(int)
    for row in table:
        field, *lang = row.split()
        res[field] = 0
        for lang_name, point in zip(lang, range(5, 0, -1)):
            if lang_name in languages:
                res[field] += point * l_per_p[lang_name]
                
    res = sorted(res.items(), key=lambda x: (-x[1], x[0]))
    answer = res[0][0]
    
    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
print(solution(table, languages, preference))