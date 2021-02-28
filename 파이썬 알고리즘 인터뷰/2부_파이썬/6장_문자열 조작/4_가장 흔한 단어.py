# 풀이 1. 리스트 컴프리헨션, Counter 객체 사용
from typing import List
import re
import collections


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]

    counts = collections.Counter(words)
    # 가장 흔하게 등항하는 단어의 첫 번째 인덱스 리턴s
    return counts.most_common(1)[0][0]