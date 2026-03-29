class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        def countofn(n):
            return (count[n],-n)
        return sorted(nums,key= countofn)