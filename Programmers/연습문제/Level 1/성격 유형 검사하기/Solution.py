def solution(survey, choices):
    global result

    result = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for types, choice in zip(survey, choices):
        addPoint(types, choice)

    return getAnswer(result)


def addPoint(survey, choice):
    global result

    if choice == 1:
        result[survey[0]] += 3
    elif choice == 2:
        result[survey[0]] += 2
    elif choice == 3:
        result[survey[0]] += 1
    elif choice == 4:
        pass
    elif choice == 5:
        result[survey[1]] += 1
    elif choice == 6:
        result[survey[1]] += 2
    elif choice == 7:
        result[survey[1]] += 3


def getAnswer(result):
    answer = ""

    if result["R"] < result["T"]:
        answer += "T"
    else:
        answer += "R"

    if result["C"] < result["F"]:
        answer += "F"
    else:
        answer += "C"

    if result["J"] < result["M"]:
        answer += "M"
    else:
        answer += "J"

    if result["A"] < result["N"]:
        answer += "N"
    else:
        answer += "A"

    return answer


if __name__ == "__main__":
    print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))