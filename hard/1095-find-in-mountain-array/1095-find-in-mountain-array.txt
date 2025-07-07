        l, r = 0, peak - 1
        while l <= r:
        # Search left portion
            else:
                break
        peak = m
            elif left > mid > right:
                r = m - 1
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
        while l <= r:
            m = (l + r) // 2
        # Find Peak
        l, r = 1, length - 2
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
#    def length(self) -> int:
# """
#class MountainArray:
#    def get(self, index: int) -> int:
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """