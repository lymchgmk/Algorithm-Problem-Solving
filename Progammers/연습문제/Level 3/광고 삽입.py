import datetime as dt


def solution(play_time, adv_time, logs):
    def adv_run_time(log_start, log_end, adv_start, adv_end):
        if adv_end < log_start or adv_start > log_end:
            return dt.timedelta(seconds=0)
        
        tmp = sorted([log_start, log_end, adv_start, adv_end])
        return tmp[2] - tmp[1]
    
    play_h, play_m, play_s = map(int, play_time.split(':'))
    dt_play_time = dt.timedelta(hours=play_h, minutes=play_m, seconds=play_s)
    adv_h, adv_m, adv_s = map(int, adv_time.split(':'))
    dt_adv_time = dt.timedelta(hours=adv_h, minutes=adv_m, seconds=adv_s)
    dt_logs = []
    for log in logs:
        log_start, log_end = log.split('-')
        start_h, start_m, start_s = map(int, log_start.split(':'))
        end_h, end_m, end_s = map(int, log_end.split(':'))
        dt_log_start, dt_log_end = dt.timedelta(hours=start_h, minutes=start_m, seconds=start_s), dt.timedelta(hours=end_h, minutes=end_m, seconds=end_s)
        dt_logs.append([dt_log_start, dt_log_end])
        
    answer = []
    for adv_start in range((dt_play_time-dt_adv_time).seconds + 1):
        dt_adv_start = dt.timedelta(seconds=adv_start)
        dt_adv_end = dt_adv_start + dt_adv_time
        adv_run_time_sum = dt.timedelta(seconds=0)
        for dt_log_start, dt_log_end in dt_logs:
            adv_run_time_sum += adv_run_time(dt_log_start, dt_log_end, dt_adv_start, dt_adv_end)
        answer.append([adv_run_time_sum, adv_start])
    answer.sort(key=lambda x: (-x[0], x[1]))

    return str(dt.timedelta(seconds=answer[0][1])).zfill(8)

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))
