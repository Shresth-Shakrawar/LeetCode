    def mirrorDistance(self, n: int) -> int:
        rev, x=0, n
        while x>0:
            x, r= x//10, x%10
            rev=10*rev+r
        return abs(rev-n)
        
class Solution: