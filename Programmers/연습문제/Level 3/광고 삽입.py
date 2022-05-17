import datetime as dt


def solution(play_time, adv_time, logs):
    def str_to_time(str_time):
        h, m, s = map(int, str_time.split(':'))
        return int(dt.timedelta(hours=h, minutes=m, seconds=s).total_seconds())
    
    def time_to_str(int_time):
        int_h, int_time = divmod(int_time, 3600)
        int_m, int_s = divmod(int_time, 60)
        str_h, str_m, str_s = str(int_h).zfill(2), str(int_m).zfill(2), str(int_s).zfill(2)
        return ':'.join([str_h, str_m, str_s])
    
    dt_play_time = str_to_time(play_time)
    dt_adv_time = str_to_time(adv_time)
    total_time = [0]*(dt_play_time+1)

    for log in logs:
        log_start, log_end = log.split('-')
        dt_log_start, dt_log_end = str_to_time(log_start), str_to_time(log_end)
        total_time[dt_log_start] += 1
        total_time[dt_log_end] -= 1

    for i in range(1, dt_play_time):
        total_time[i] += total_time[i-1]

    for i in range(1, dt_play_time):
        total_time[i] += total_time[i-1]

    answer, max_time = 0, 0
    for i in range(dt_adv_time-1, dt_play_time):
        if i >= dt_adv_time:
            if max_time < total_time[i] - total_time[i - dt_adv_time]:
                max_time = total_time[i] - total_time[i - dt_adv_time]
                answer = i - dt_adv_time + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                answer = i - dt_adv_time + 1

    return time_to_str(answer)


play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time, adv_time, logs))
