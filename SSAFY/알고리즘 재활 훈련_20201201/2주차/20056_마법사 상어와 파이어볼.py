import sys
sys.stdin = open('20056_마법사 상어와 파이어볼.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


N, M, K = map(int, input().split())
FB = [list(map(int, input().split())) for _ in range(M)]
for _ in range(K):
    #1 이동
    dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    for i in range(len(FB)):
        s, d = FB[i][3], FB[i][4]
        FB[i][0] = (FB[i][0] + dir[d][0]*s) % N + 1
        FB[i][1] = (FB[i][1] + dir[d][1]*s) % N + 1
        
    #2 합치기
    FB_dict = dict()
    for fb in FB:
        key, val = tuple(fb[:2]), tuple(fb[2:])
        if key not in FB_dict.keys():
            FB_dict[key] = val
        else:
            FB_dict[key] += val

    FB = []
    for fb in FB_dict.items():
        x, y = fb[0]
        fb_cnt = len(fb[1])//3
        if fb_cnt >= 2:
            sum_m, sum_s, sum_d = 0, 0, []
            for i in range(len(fb[1])):
                if i % 3 == 0:
                    sum_m += fb[1][i]
                elif i % 3 == 1:
                    sum_s += fb[1][i]
                elif i % 3 == 2:
                    sum_d.append(fb[1][i])
            
            check_d = sum_d[0]
            for d in sum_d:
                if d%2 != check_d%2:
                    flag_d = False
                    break
            else:
                flag_d = True

            for i in range(4):
                if flag_d == False:
                    d = 2*i+1
                else:
                    d = 2*i
                m, s = int(sum_m/5), int(sum_s/fb_cnt)
                if m != 0:
                    FB.append([x, y, m, s, d])

        else:
            m, s, d = fb[1]
            if m != 0:
                FB.append([x, y, m, s, d])

answer = 0
for fb in FB:
    answer += fb[2]
print(answer)