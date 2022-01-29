def solution(id_list, report, k):
    result = {id: set() for id in id_list}
    for _report in report:
        reporter, reported = _report.split()
        result[reporter].add(reported)

    counter = {id: 0 for id in id_list}
    for reported in result.values():
        for _reported in reported:
            counter[_reported] += 1

    answer = []
    for id in id_list:
        _tmp = 0
        for reported in result[id]:
            if counter[reported] >= k:
                _tmp += 1
        answer.append(_tmp)
    return answer


if __name__ == "__main__":
    # TC 1
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
    k = 2
    print(solution(id_list, report, k)) # [2, 1, 1, 0]