def solution(phone_number):
    import re

    return re.sub('\d(?=\d{4})', '*', phone_number)

print(solution("0277788889999"))