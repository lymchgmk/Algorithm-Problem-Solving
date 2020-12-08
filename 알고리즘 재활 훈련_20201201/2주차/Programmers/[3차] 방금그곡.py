import sys

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# musicinfos = ["12:00,12:14,HELLO,C#DEC#FGAB", "13:00,13:05,WORLD,ABC#DEF"]

def solution(m, musicinfos):
    answer = []


    def tokenize(sample):
        sample = sample.replace('C#', 'c')
        sample = sample.replace('D#', 'd')
        sample = sample.replace('F#', 'f')
        sample = sample.replace('G#', 'g')
        sample = sample.replace('A#', 'a')
        
        return sample


    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))

        m, music = tokenize(m), tokenize(music)

        time = (end_h-start_h)*60 + (end_m-start_m)
        repeat = time//len(music) + 1
        music = (music*repeat)[:time]
        
        if len(music) < len(m):
            continue

        for i in range(len(music)-len(m)+1):
            for j in range(len(m)):
                if music[i+j] != m[j]:
                    break
            else:
                if not answer:
                    answer = [len(music), title]
                else:
                    if answer[0] < len(music):
                        answer = [len(music), title]
                break
                
    if not answer:
        answer = '(None)'
    else:
        answer = answer[1]
        
    return answer

        
print(solution(m, musicinfos))