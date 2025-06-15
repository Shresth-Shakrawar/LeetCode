class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequenceStarters: list[int]= []
        numSet=set(nums)
        for num in numSet:
            if num-1 not in numSet:
                sequenceStarters.append(num)
        maxLength=0
        for i in sequenceStarters:
            start=i
            length=1
            while start+1 in numSet:
                start+=1
                length+=1
            maxLength=max(length,maxLength)
        return maxLength
            



        