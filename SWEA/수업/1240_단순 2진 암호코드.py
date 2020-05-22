import sys
sys.stdin=open('1240_단순 2진 암호코드.txt')

def decoder(sample):
    if sample==13: return 0
    elif sample==25: return 1
    elif sample==19: return 2
    elif sample==61: return 3
    elif sample==35: return 4
    elif sample==49: return 5
    elif sample==47: return 6
    elif sample==59: return 7
    elif sample==55: return 8
    elif sample==11: return 9
    else: return 'X'

def scanner(test_sample):
    test_temp='0b'+ ''.join(test_sample)
    sample=int(test_temp, 2)
    return sample

T=int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    crypto=[input() for _ in range(N)]
    do_test=0
    data=[]

    for code in crypto:
        if code != '0'*M:
            sample=code
            break

    for i in range(len(code)-1, -1, -1):
        if code[i] == '1':
            decoded_sample=code[i-55:i+1]
            break

    for i in range(0,len(decoded_sample)//7):
        temp=scanner(decoded_sample[i*7:i*7+7])
        data.append(decoder(temp))

    parity=data.pop()
    sum_odd, sum_even = 0, 0
    for i in range(8):
        if i!=7:
            if i%2:
                sum_even += data[i]
            else:
                sum_odd += data[i]

    ans=0
    if (sum_odd*3+sum_even+parity)%10 == 0:
        ans=sum_odd+sum_even+parity

    print(f'#{test_case} {ans}')