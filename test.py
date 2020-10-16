def hansoo(x):
    answer = 0
    for n in range(1, x+1):
        n_list = list(map(int, list(str(n))))
        L = len(n_list)

        if 0 < L <= 2:
            answer += 1
            continue

        else:
            if n_list[0]-n_list[1] == 0:
                answer += 1
                continue
            else:
                test = list(range(n_list[0], 10, n_list[1]-n_list[0]))[:L]
                test_r = list(range(n_list[0], -1, n_list[1]-n_list[0]))[:L]
                print(n, test, test_r, n_list)
                if n_list == test or n_list == test_r:
                    print(999)
                    answer += 1
    
    return answer
            

X = 210
print(hansoo(X))
