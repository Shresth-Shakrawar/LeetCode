class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        for val in nums:
            if val in count.keys():
                count[val]+=1
            else:
                count[val]=1
        sol=[]
        n=len(nums)
        for val,freq in count.items():
            if freq >n/3:
                sol.append(val)
        return sol