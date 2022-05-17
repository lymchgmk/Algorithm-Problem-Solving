import collections


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_tree_list = list(skill_tree)
        skill_deq = collections.deque(skill)
        
        for s in skill_tree_list:
            if s in skill_deq:
                if s != skill_deq.popleft():
                    break
        else:
            answer += 1
    
    return answer
    

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))