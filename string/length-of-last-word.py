class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l= s.split(" ")
        i = 1
        while l[-i] == "":
            i+=1

        return len(l[-i])