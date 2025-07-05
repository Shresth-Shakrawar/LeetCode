class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eSum = 0
        dSum = 0
        for n in nums:
            eSum += n
            nStr = str(n)
            for c in nStr:
                dSum += int(c)
        return abs(dSum - eSum)