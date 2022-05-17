def solution(str1, str2):
    def make_set(s):
        result = []
        for c1, c2 in zip(s[:-1], s[1:]):
            if not c1.isalpha() or not c2.isalpha():
                continue
            else:
                c1, c2 = c1.lower(), c2.lower()
                result.append(c1+c2)
        return result
    
    def jacard(list1, list2):
        from collections import Counter
        
        if not list1 and not list2:
            return 1
        
        cntr1, cntr2 = Counter(list1), Counter(list2)
        union = cntr1+cntr2
        inter = {}
        for key1, val1 in cntr1.items():
            val2 = cntr2[key1]
            if key1 in cntr2:
                inter[key1] = min(val1, val2)
                union[key1] = max(val1, val2)
                
        return sum(inter.values()) / sum(union.values())
    
    list1, list2 = make_set(str1), make_set(str2)
    
    return int(jacard(list1, list2)*65536)


str1 = 	"aa1+aa2"
str2 = 	"AAAA12"
print(solution(str1, str2))