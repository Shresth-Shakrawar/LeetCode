class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1= 0
        answer2= 0
        for i,n in enumerate(nums1):
            if n in nums2:
                answer1 += 1
    
        for i,n in enumerate(nums2):
            if n in nums1:
                answer2 += 1
        return [answer1,answer2]
        