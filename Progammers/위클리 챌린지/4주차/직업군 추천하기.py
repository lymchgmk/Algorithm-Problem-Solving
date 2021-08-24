def solution(table, languages, preference):
    preference_dict = {key: value for key in languages for value in preference}
    table_dict = {}
    for row in table:
        key, *values = row.split()
        table_dict[key] = values
        
    print(table_dict)
    print(preference_dict)


if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]
    
    print(solution(table, languages, preference))
    