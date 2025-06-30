class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        wordSet = set(allowed)
        for w in words:
            for ch in w:
                if ch not in wordSet:
                    count -= 1
                    break
        return count