class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numSet =set(nums)
        while original <= 1000:
            if original in numSet:
                original *= 2 
            else:
                break
        return original
            