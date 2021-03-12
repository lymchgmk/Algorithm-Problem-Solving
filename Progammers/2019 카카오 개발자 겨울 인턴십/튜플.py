import sys
sys.stdin = open('튜플.txt', 'rt')
import collections


input = lambda: sys.stdin.readline().strip()
def solution(s):
    tmp_s = ''
    for char in s:
        if char not in ("'", '"', '{', '}'):
            tmp_s += char
    tmp_lst = tmp_s.split(',')
    tmp_counter = collections.Counter(tmp_lst).most_common(len(tmp_lst))
    answer = [int(num[0]) for num in tmp_counter]
    
    return answer

print(solution(input()))