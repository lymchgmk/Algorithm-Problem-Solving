import re


def solution(s):
    for x in s:
        finditer = re.finditer(r'(110)', x)
        while True:
            try:
                span = finditer.__next__().span()
                x = x[:span[0]] + x[span[1]:]
                print('x', x)
                for idx in range(len(x)):
                    tmp = x[:idx] + '110' + x[idx:]
                    print(tmp)
            except StopIteration:
                break
        # tmp = re.search(r'(110)', x)
        # print(x, tmp)
        # print(re.split(r'(110)', x))
        
        
        
s = ["1110","100111100","0111111010"]
print(solution(s))
