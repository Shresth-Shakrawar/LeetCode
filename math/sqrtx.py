class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            mid = (l+r)//2
            if mid ** 2 == x :
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1
        
        return r