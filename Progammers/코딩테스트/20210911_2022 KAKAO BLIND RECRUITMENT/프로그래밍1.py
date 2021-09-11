from collections import defaultdict


def solution(id_list, report, k):
    report_dict, ban_counter = defaultdict(set), defaultdict(int)
    for reported in report:
        reporter, target = reported.split()
        if target not in report_dict[reporter]:
            report_dict[reporter].add(target)
            ban_counter[target] += 1

    banned_user = [user for user in ban_counter if ban_counter[user] >= k]
    answer = []
    for id in id_list:
        reported_list = report_dict[id]
        cnt = 0
        for reported in reported_list:
            if reported in banned_user:
                cnt += 1
        answer.append(cnt)
    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# print(solution(id_list, report, k)) # [2, 1, 1, 0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
print(solution(id_list, report, k)) # [2, 1, 1, 0]