info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

L = len(info)
test_info, test_query = [], []

for i in info:
    test_info.append(i.split())

for q in query:
    temp1 = q.split(' ')
    temp2 = []
    for t in temp1:
        if t != 'and':
            temp2.append(t)
    test_query.append(temp2)

# print('test_info', test_info)
# print('test_query', test_query)

answer = []

for i in range(L):
    result = 6

    tq = test_query[i]
    for j in range(L):
        ti = test_info[j]
        print('tq', tq)
        print('ti', ti, j)
        for i in range(5):
            if tq[i] != '-' and tq[i].isalpha() and tq[i] != ti[i]:
                result -= 1
                break
            elif tq[i] != '-' and tq[i].isdecimal() and int(tq[i]) > int(ti[i]):
                result -= 1
                break

    answer.append(result)

