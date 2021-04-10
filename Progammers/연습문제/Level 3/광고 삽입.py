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
    dt_answer_candidates = [[dt.timedelta(seconds=0), dt_adv_time]]
    for log in logs:
        log_start, log_end = log.split('-')
        start_h, start_m, start_s = map(int, log_start.split(':'))
        end_h, end_m, end_s = map(int, log_end.split(':'))
        dt_log_start, dt_log_end = dt.timedelta(hours=start_h, minutes=start_m, seconds=start_s), dt.timedelta(hours=end_h, minutes=end_m, seconds=end_s)
        dt_logs.append([dt_log_start, dt_log_end])
        if dt_log_end - dt_adv_time >= dt.timedelta(seconds=0):
            dt_answer_candidates.append([dt_log_end - dt_adv_time, dt_log_end])
        if dt_log_start + dt_adv_time <= dt_play_time:
            dt_answer_candidates.append([dt_log_start, dt_log_start + dt_adv_time])
    
    answer = [dt.timedelta(seconds=0), dt.timedelta(seconds=0)]
    for candidate in dt_answer_candidates:
        sum_adv_time = dt.timedelta(seconds=0)
        for log in dt_logs:
            sum_adv_time += adv_run_time(log[0], log[1], candidate[0], candidate[1])
        if answer[1] < sum_adv_time or (answer[1] == sum_adv_time and answer[0] > candidate[0]):
            answer = [candidate[0], sum_adv_time]

    return str(answer[0]).zfill(8)


play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
print(solution(play_time, adv_time, logs))
