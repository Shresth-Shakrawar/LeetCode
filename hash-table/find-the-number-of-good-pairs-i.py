class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        cnt = 0
        for i in nums1:
            for j in nums2:
                if i % (j * k) == 0:
                    cnt += 1
        return cnt