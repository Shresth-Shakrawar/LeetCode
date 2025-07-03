class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            minIndex = -1
            minNum = float("inf")
            for i,n in enumerate(nums):
                if n < minNum:
                    minNum = n
                    minIndex = i
                else:
                    continue
            nums[minIndex] *= multiplier
        return nums



                