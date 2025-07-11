class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums={0:1} # empty Subarray
        res=0
        curSum=0
        for n in nums:
            curSum += n
            diff= curSum -k

            res= res +prefixSums.get(diff,0)
            prefixSums[curSum]= 1+prefixSums.get(curSum,0)
        return res
        