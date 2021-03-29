import re


# 특정 단어 제거('and' 제거 예시)
re.findall(r'[-]|\b(?!and\b)\w+', q)