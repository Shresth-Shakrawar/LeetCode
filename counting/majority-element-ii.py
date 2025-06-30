class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = floor(len(nums) / 3)
        res = []
        freq = Counter(nums)

        for val, count in freq.items():
            if count > target:
                res.append(val)
        
        return res