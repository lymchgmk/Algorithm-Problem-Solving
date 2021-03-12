import re


def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    # 2
    for char in new_id:
        if char in "~!@#$%^&*()=+[{]}:?,<>/":
            new_id = new_id.replace(char, '')
    
    # 3
    p = re.compile(r'.+')
    new_id = p.sub('.', new_id)
    print(new_id)
    
    # 4
    if new_id[0] == '.':
        new_id = new_id[1:]
    try:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    except IndexError:
        pass
    
    # 5
    if not new_id:
        new_id = 'a'
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:14]
    
    # 7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    
    answer = new_id
    return answer


new_id = "=.="
print('answer :', solution(new_id))


import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st