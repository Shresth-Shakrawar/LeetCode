from heapq import heapify,heappop
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        intersection = set1.intersection(set2)
        if intersection:
            return min(intersection)
        return -1