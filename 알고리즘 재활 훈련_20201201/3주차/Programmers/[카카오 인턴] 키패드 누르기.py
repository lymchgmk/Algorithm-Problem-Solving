import sys


def solution(numbers, hand):
    answer = ''
    left_thumb, right_thumb = '*', '#'
    only_left = [1, 4, 7]
    only_right = [3, 6, 9]


    def thumb_dist(thumb, target):
        if thumb == '*':
            thumb_row, thumb_col = 3, 1
        elif thumb == '#':
            thumb_row, thumb_col = 3, 3
        elif thumb == 0:
            thumb_row, thumb_col = 3, 2
        else:
            thumb_row, thumb_col = divmod(thumb, 3)
            if thumb % 3 == 0:
                thumb_row -= 1
                thumb_col += 1
        
        if target != 0:
            target_row, target_col = divmod(target, 3)
        else:
            target_row, target_col = 3, 2

        return abs(thumb_row - target_row) + abs(thumb_col - target_col)


    for n in numbers:
        if n in only_left:
            answer += 'L'
            left_thumb = n
        elif n in only_right:
            answer += 'R'
            right_thumb = n
        else:
            if thumb_dist(left_thumb, n) < thumb_dist(right_thumb, n):
                answer += 'L'
                left_thumb = n
            elif thumb_dist(left_thumb, n) > thumb_dist(right_thumb, n):
                answer += 'R'
                right_thumb = n
            else:
                if hand == 'left':
                    answer += 'L'
                    left_thumb = n
                else:
                    answer += 'R'
                    right_thumb = n
    
    return answer


if __name__ == "__main__":
    numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand = 'left'
    print(solution(numbers, hand))