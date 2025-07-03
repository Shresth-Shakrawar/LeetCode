class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i,ch in enumerate(s,start =1):
            temp = ord("z") - ord(ch)  +1
            ans = ans + temp*i     
        return ans