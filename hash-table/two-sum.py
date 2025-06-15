class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}   # val-> index
        for i,n in enumerate(nums):     #enumerate(num) returns index->val
            diff = target- n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[n]=i   # Appends val->index to Hashmap
             



        