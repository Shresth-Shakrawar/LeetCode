class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ##print(f"{len(nums)=}")
    #Negative Marking Values Has 3 steps:
        #Step 1: Assign all negative numbers to zero
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        ##print(f"After making negatives zero {nums=}")
        
        #Step 2:Mark All The Positive To Index In The Array Itself
        for i in range(len(nums)):
            val=abs(nums[i])        # After Marking Indexes As Negative We Still Have To Check
            if val>0 and val<=len(nums):
                index=val-1         # For Value 3 we mark i=2 as negative
                if nums[index]>0:
                    nums[index]= -1 * (nums[index])
                elif nums[index]==0:# If nums[index] is assigned to zero we mark it as out of bound (len(nums)+1)
                    nums[index]= -1 * (len(nums)+1)
        
        ##print(f"After Negative Marking {nums=}")
        
        # Step 3 : Checking If Index Is Marked Or Not
        for i in range(len(nums)):
            if(nums[i]>=0):
                return i+1
            #If all indexes Marked we return First out of bounds element [len(nums)+1]
        return len(nums)+1
