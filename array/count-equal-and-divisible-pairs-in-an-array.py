class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]==nums[j] and (i*j) % k == 0: 
                    res +=1
        return res