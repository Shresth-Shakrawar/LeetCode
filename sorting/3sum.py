class Solution:
    #nums[i] +nums[j]+nums[k] ==0
    #-nums[i]= nums[j]+nums[k]
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol=[]
        seen=[]
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.append(nums[i])
            j,k=i+1,len(nums)-1
            target=-nums[i]
            
            while j<k:
                if nums[j]+nums[k]==target:
                    sol.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    while nums[j]==nums[j-1] and j<k:
                        j=j+1
                elif nums[j]+nums[k] < target:
                    j=j+1
                elif nums[j]+nums[k] >target:
                    k=k-1
                
        return sol




        