class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap={}       # Stores Last Index Where Number was Encountered{1:0,2:1,3:2}[1 encountered at 0]
        for i,num in enumerate(nums):
            if num in indexMap and i-indexMap[num] <=k:
                return True
            else:
                indexMap[num]= i
        return False
            


        
        
        
        