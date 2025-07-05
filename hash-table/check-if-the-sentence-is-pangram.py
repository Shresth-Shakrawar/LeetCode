class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s =set(sentence)
        return True if len(s) == 26 else False