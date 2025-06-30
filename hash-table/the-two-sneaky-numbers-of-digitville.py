class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        numSet=set()
        res = set()
        for num in nums:
            if num in numSet:
                res.add(num)
            else:
                numSet.add(num)
        return list(res)