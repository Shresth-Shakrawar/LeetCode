from collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = Counter(word)
        combinations = 1
        for ch,freq in count.items():
            if freq > 1:
                combinations += (freq - 1)
        return combinations