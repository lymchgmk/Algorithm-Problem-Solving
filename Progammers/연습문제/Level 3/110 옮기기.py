# import re
#
#
# def solution(s):
#     # 1. 제일 뒤에 있는 110을 찾기
#     for x in s:
#         rev_x = x[::-1]
#         rev_pattern = r'(011)'
#         rev_finditer = re.finditer(rev_pattern, rev_x)
#         while True:
#             try:
#                 rev_span = finditer.__next__().span()
#                 x = x[:span[0]] + x[span[1]:]
#                 print('x', x)
#                 for idx in range(len(x)):
#                     tmp = x[:idx] + '110' + x[idx:]
#                     print(tmp)
#             except StopIteration:
#                 break
#         # tmp = re.search(r'(110)', x)
#         # print(x, tmp)
#         # print(re.split(r'(110)', x))
import re


def solution(s):
    answer = []
    for x in s:
        # 1. '110' 제거
        cnt = 0
        while True:
            post_x = re.sub(pattern=r'(110)', repl='', string=x)
            if x == post_x:
                break
            x = post_x
            cnt += 1

        print(x, cnt)
        # 2. '110' 삽입
        while cnt:
            for i in range(len(x)-1, -1, -1):
                if x[i] == '0':
                    print(x)
                    x = x[:i] + '110' + x[i:]
                    print(x)
            cnt -= 1

    return answer
        
        
s = ["1110","100111100","0111111010"]
print(solution(s))
