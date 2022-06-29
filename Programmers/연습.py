def solution(word):
    def str2hex(input_str):
        return str(hex(int(input_str, 2)))[-1]

    bitmap_fonts = {}
    if len(word) <= 16:
        n_word = word.rjust(16, " ")
        answer = [["0x"] * 16 for _ in range(8)]
    elif 16 < len(word) <= 32:
        n_word = word.rjust(32, " ")

    for char in n_word:
        print(char, n_word)
        font = bitmap_fonts[char]
        for row in font:
            front, back = row[:4], row[4:]
            str2hex(front) + str2hex(back)


if __name__ == "__main__":
    word = "1 "
    print(solution(word))