# import sys
# sys.stdin = open("test.txt", "r")

# 모든 막대는 다 연결된다.
# 같은 막대는 없다
import sys
sys.stdin = open("test.txt", "r")

def find_start_bolt(bolt_and_nut):
    start_bolt = []

    for bolt in bolt_and_nut:
        if bolt_and_nut.count(bolt) == 1:
            start_bolt.append(bolt)

    if bolt_and_nut.index(start_bolt[0]) % 2 == 0:
        return bolt_and_nut[bolt_and_nut.index(start_bolt[0]): bolt_and_nut.index(start_bolt[0])+2]
    else:
        return bolt_and_nut[bolt_and_nut.index(start_bolt[1]): bolt_and_nut.index(start_bolt[1])+2]


T = int(input())

for test_case in range(1, T+1):
    BnN_num = int(input())
    bolt_and_nut = list(map(int, input().split()))

    bolts = [bolt_and_nut[i:i+2] for i in range(0, len(bolt_and_nut)) if i%2==0]
    start_bolt = find_start_bolt(bolt_and_nut)
    bolt_chain = [] + start_bolt

    count = 0
    while count < len(bolts):
        for bolt in bolts:
            if bolt_chain[-1] == bolt[0]:
                bolt_chain.extend(bolt)
        count += 1

    print('#{}'.format(test_case), end=' ')
    for b in bolt_chain:
        print(b, end=' ')
    print()

#    result = ' '.join(map(str, bolt_chain))
#    print("#{0} {1}".format(test_case, result))