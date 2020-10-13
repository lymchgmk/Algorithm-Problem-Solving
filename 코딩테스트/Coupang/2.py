def solution(n, customers):
    kiosk = [[False, [None, None, None]]] * n
    print(kiosk)
    how_many = [0]*n
    now_time = None

    for customer in customers:
        date, time, how_long = customer.split()
        date = list(map(int, date.split('/')))
        time = list(map(int, time.split(':')))

        now_time = [date, time]

        for k in kiosk:
            if not k[0]:
                k[1][0], k[1][1], k[1][2] = date, time, how_long
                k[0] = True
                break
            
            



    return 0





n = 3
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

print(solution(n, customers))