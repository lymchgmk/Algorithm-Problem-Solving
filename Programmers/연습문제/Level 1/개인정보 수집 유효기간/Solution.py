def solution(today, terms, privacies):
    check_terms = {}
    for term in terms:
        item, time = term.split()
        check_terms[item] = int(time) * 28

    def deprecated(privacy):
        today_list = list(map(int, today.split('.')))
        today2day = today_list[0] * (12 * 28) + today_list[1] * 28 + today_list[2]

        privacy_info, privacy_name = privacy.split()
        privacy_list = list(map(int, privacy_info.split('.')))
        privacy2day = privacy_list[0] * (12 * 28) + privacy_list[1] * 28 + privacy_list[2]

        return today2day - privacy2day < check_terms[privacy_name]

    return [idx for idx, privacy in enumerate(privacies, start=1) if not deprecated(privacy)]


if __name__ == "__main__":
    today = "2022.05.19"
    terms = ["A 6", "B 12", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    result = [1, 3]
    print(solution(today, terms, privacies))