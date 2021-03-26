def solution(s):
    def binary_trans(s):
        count_0, count_1 = s.count('0'), s.count('1')
        s = '1'*count_1
        return count_0, bin(len(s))
    
    cnt_0, cnt_trans = 0, 0
    while s != '1':
        cnt_tmp, s_tmp = binary_trans(s)
        s = s_tmp[2:]
        cnt_0 += cnt_tmp
        cnt_trans += 1
    
    return [cnt_trans, cnt_0]


s = "110010101001"
print(solution(s))
