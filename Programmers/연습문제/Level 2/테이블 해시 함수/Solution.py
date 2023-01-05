def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    rows = zip(range(row_begin, row_end+1), data[row_begin - 1: row_end])

    answer = 0
    for idx, row in rows:
        _sum = 0
        for element in row:
            _sum += element % idx
        answer ^= _sum

    return answer


if __name__ == "__main__":
    data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
    col = 2
    row_begin = 2
    row_end = 3
    print(solution(data, col, row_begin, row_end)) # 4