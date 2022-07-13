def solution(name):
    def count_stick(char):
        return min(ord(char) - 65, 90 - ord(char) + 1)

    count_updown = sum(count_stick(char) for char in name if char != 'A')

    count_leftright = len(name) - 1
    for idx in range(len(name)):
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        distance = min(idx, len(name) - next_idx)
        count_leftright = min(count_leftright, idx + len(name) - next_idx + distance)

    return count_updown + count_leftright


if __name__ == "__main__":
    name = "BABBBB"
    print(solution(name))
