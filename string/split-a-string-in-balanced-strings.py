class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, bal = 0, 0 #balance
        for car in s:
            if car == "L":
                bal += 1
            else:
                bal -= 1
            
            if bal == 0:
                cnt += 1
        return cnt