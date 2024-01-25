from typing import List
import re


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        for word in sorted(dictionary, key=lambda x: (-len(x), x)):
            s = re.sub(word, "", s)