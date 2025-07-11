class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        words.sort(key = lambda x: int(x[-1]))
        return " ".join(word[:-1] for word in words)