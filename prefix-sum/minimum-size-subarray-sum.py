class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        suma=0
        l=0
        minL = float("inf")
        for r in range(len(nums)):
            suma = suma + nums[r]
            #print(f"start {l=} {r=} {suma=}")
            while suma >= target :
                minL = min( minL , (r-l) + 1 )
                suma = suma - nums[l]
                l += 1
            #print(f"after {l=} {r=} {suma=} {minL=}")
        if minL != float("inf"):
            return minL
        else:
            return 0
