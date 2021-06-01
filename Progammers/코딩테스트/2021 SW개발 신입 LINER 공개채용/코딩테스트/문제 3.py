def solution(enter, leave):
    answer = {i: set() for i in range(1, len(enter) + 1)}
    for man in range(1, len(enter) + 1):
        for target in range(1, len(enter) + 1):
            if man != target:
                man_enter, man_leave = enter.index(man), leave.index(man)
                target_enter, target_leave = enter.index(target), leave.index(target)
                
                if (man_enter > target_enter and target_leave > man_leave) or (man_enter < target_enter and target_leave < man_leave):
                    answer[man].add(target)
                    answer[target].add(man)
                
                elif man_enter < target_enter and man_leave == target_enter:
                    answer[man].add(target)
                    answer[target].add(man)
                    
    res = [len(val) for val in answer.values()]
    return res


enter = [1,4,2,3]
leave = [2,1,4,3]
print(solution(enter, leave))
