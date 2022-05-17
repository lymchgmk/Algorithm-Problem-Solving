def solution(table, languages, preference):
    preference_dict = {key: value for key, value in zip(languages, preference)}
    
    table_dict = {}
    for row in table:
        key, *langs = row.split()
        table_dict[key] = {lang: len(langs) - idx for idx, lang in enumerate(langs)}
        
    result_dict = {field: 0 for field in table_dict}
    for field in table_dict:
        for lang, weight in preference_dict.items():
            try:
                result_dict[field] += table_dict[field][lang] * weight
            except KeyError:
                continue
    
    answer = sorted(result_dict.items(), key=lambda x: (-x[1], x[0]))[0][0]
    return answer
        

if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]
    
    print(solution(table, languages, preference))
    