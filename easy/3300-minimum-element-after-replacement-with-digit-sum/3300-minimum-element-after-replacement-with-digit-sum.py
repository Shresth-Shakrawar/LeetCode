class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_= float("inf")
        for n in nums:
            s = str(n)
            temp = 0
            for ch in s:
                temp += int(ch)
            min_ = min(min_,temp)
        return min_