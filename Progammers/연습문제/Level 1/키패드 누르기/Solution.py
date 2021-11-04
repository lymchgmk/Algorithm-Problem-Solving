def thumb_dist(keyboard_dict, thumb, target):
    thumb_row, thumb_col= keyboard_dict[thumb]
    target_row, target_col = keyboard_dict[target]
    return abs(thumb_row - target_row) + abs(thumb_col - target_col)


def solution(numbers, hand):
    answer = ""
    keyboard_dict = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2),
        "*": (3, 0), "0": (3, 1), "#": (3, 2)
    }
    left_thumb, right_thumb = "*", "#"
    only_left_thumb, only_right_thumb = ["1", "4", "7"], ["3", "6", "9"]
    for target in numbers:
        target = str(target)
        if target in only_left_thumb:
            answer += "L"
            left_thumb = target
        elif target in only_right_thumb:
            answer += "R"
            right_thumb = target
        else:
            left_thumb_dist = thumb_dist(keyboard_dict, left_thumb, target)
            right_thumb_dist = thumb_dist(keyboard_dict, right_thumb, target)
            if left_thumb_dist < right_thumb_dist:
                answer += "L"
                left_thumb = target
            elif left_thumb_dist > right_thumb_dist:
                answer += "R"
                right_thumb = target
            else:
                if hand == "left":
                    answer += "L"
                    left_thumb = target
                else:
                    answer += "R"
                    right_thumb = target
    return answer