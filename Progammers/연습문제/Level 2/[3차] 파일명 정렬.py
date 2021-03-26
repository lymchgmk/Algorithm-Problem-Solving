import re


def solution(files):
    pattern = re.compile('(\D+)(\d+)(.*)')
    head_number_tail = list(enumerate([re.findall(pattern, file)[0] for file in files]))
    head_number_tail.sort(key=lambda x: (x[1][0].lower(), int(x[1][1]), x[0]))
    
    answer = []
    for _, h_n_t in head_number_tail:
        answer.append(''.join(h_n_t))
    return answer


files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))