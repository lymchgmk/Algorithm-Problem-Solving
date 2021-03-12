import re
import itertools


def isMatch(user_perm, banned_id):
    for user in user_perm:
        for ban in banned_id:
            pass
        
    # for i in range(len(user_set)):
    #     if len(user_set[i]) != len(banned_set[i]):
    #         return False
    #
    #     for j in range(len(user_set[i])):
    #         if banned_set[i][j] == '*':
    #             continue
    #         if user_set[i][j] != banned_set[i][j]:
    #             return False
    
    return True


def solution(user_id, banned_id):
    answer = []
    for user_perm in itertools.permutations(user_id, len(banned_id)):
        if isMatch(user_perm, banned_id):
            user_set = set(user_perm)
            if user_set not in answer:
                answer.append(user_set)
    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))