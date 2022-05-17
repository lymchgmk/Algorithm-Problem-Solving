def solution(record):
    import collections
    answer = []
    
    rec_dict = collections.defaultdict(list)
    name_dict = collections.defaultdict(str)
    for idx, rec in enumerate(record):
        op, uid, *name = rec.split()
        rec_dict[(op, uid, idx)] = name
        if name:
            name_dict[uid] = name[0]
    
    for op_id in rec_dict:
        op, uid, _ = op_id
        if op  == 'Enter':
            answer.append(f'{name_dict[uid]}님이 들어왔습니다.')
        elif op == 'Leave':
            answer.append(f'{name_dict[uid]}님이 나갔습니다.')
            
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
