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


def solution(s):
    def slice_110(input_str):
        for idx in range(len(input_str)-3, -1, -1):
            if input_str[idx:idx+3] == '110':
                return input_str[:idx] + input_str[idx+3:]
    
    answer = []
    for x in s:
        flag = True
        while flag:
            # 1. 제일 뒤의 '110' 찾기
            curr_x, sliced_x = x, slice_110(x)
            
            # 2. '110' 삽입하면서 체크
            for idx in range(len(sliced_x)):
                post_x = sliced_x[:idx] + '110' + sliced_x[idx:]
                if curr_x > post_x:
                    x = post_x
                    break
            else:
                flag = False
                answer.append(curr_x)
    
    return answer
        
        
s = ["1110","100111100","0111111010"]
print(solution(s))
