import re


def pre_rule(new_id):
    if len(new_id) < 3 or len(new_id) > 15:
        return False

    for char in new_id:
        if char not in r'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            return False
    if new_id[0] == '.' or new_id[-1] == '.':
        return False
    if new_id != re.sub('[.]{2,}', '.', new_id):
        return False

    return True


def solution(new_id):
    if pre_rule(new_id) is True: return new_id

    flag = False

    new_id = new_id.lower()

    new_id = re.sub('[~!@#$%^&*()=+\[{\]}:?,<>]', '', new_id)

    new_id = re.sub('[.]{2,}', '.', new_id)

    if new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]

    if new_id == '': new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        flag = True

    if flag == True and new_id[-1] == '.': new_id = new_id[:-1]

    step7 = new_id[-1]
    while len(new_id) <= 2: new_id += step7

    return new_id