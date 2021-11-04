import re


def solution(new_id):
    answer = ''
    
    step_0 = new_id
    step_1 = step_0.lower()
    step_2 = re.sub('[^a-z0-9-_.]', '', step_1)
    step_3 = re.sub('[.]+', '.', step_2)
    step_4 = re.sub('^[.]|[.]$', '', step_3)
    step_5 = 'a' if not step_4 else step_4
    step_6 = step_5[:15] if len(step_5) >= 16 else step_5
    step_6 = re.sub('[.]$', '', step_6)
    step_7 = step_6 if len(step_6) > 2 else step_6 + step_6[-1]*(3-len(step_6))
    
    answer = step_7
    return answer