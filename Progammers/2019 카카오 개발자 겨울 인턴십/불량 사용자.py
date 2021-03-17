from timeit import default_timer as timer
import itertools


def solution(user_id, banned_id):
    def isMatch(users, bans):
        for i in range(len(users)):
            user, ban = users[i], bans[i]
            if len(user) != len(ban):
                return False
            else:
                for j in range(len(user)):
                    user_char, ban_char = user[j], ban[j]
                    if ban[j] == '*':
                        continue
                    elif user_char != ban_char:
                        return False
        return True
    
    answer = []
    for user_perm in itertools.permutations(user_id, len(banned_id)):
        if isMatch(user_perm, banned_id):
            user_set = set(user_perm)
            if user_set not in answer:
                answer.append(user_set)
    
    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
start_time = timer()
print(solution(user_id, banned_id))
print(timer() - start_time)