import re


def solution(s):
    def remove_110(x):
        cnt = 0
        while True:
            _x = re.sub(pattern=r'(110)', repl='', string=x)
            _cnt = (len(x) - len(_x)) // 3
            if x == _x:
                break
            x = _x
            cnt += _cnt
        return x, cnt

    def insert_110(x, cnt):
        for idx in range(len(x)-1, -1, -1):
            if x[idx] == '0':
                return x[:idx+1] + '110' * cnt + x[idx+1:]
        else:
            return '110' * cnt + x

    answer = []
    for _s in s:
        _s, cnt = remove_110(_s)
        _s = insert_110(_s, cnt)
        answer.append(_s)
    return answer


s = ["1110", "100111100", "0111111010"]
# s = ["1011110","01110","101101111010"]
print(solution(s))
