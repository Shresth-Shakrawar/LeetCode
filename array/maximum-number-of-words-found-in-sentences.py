class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0
        for s in sentences:
            s_len = len(s.split(' '))
            most = max(most,s_len)
        return most