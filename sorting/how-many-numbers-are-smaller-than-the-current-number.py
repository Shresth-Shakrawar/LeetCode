class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t = sorted(nums)
        dic = {}
        for i, num in enumerate(t) :
            if num not in dic:
                dic[num] = i
        
        return [dic[x] for x in nums]