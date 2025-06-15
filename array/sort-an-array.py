class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr: list[int],l:int,r:int) -> list[int]:

            if l==r:             # Base Case For arr[size] = 1
                return arr

            m= (l+r) //2
            mergeSort(arr,l,m)   # Calling Recursively on Left Subarray
            mergeSort(arr,m+1,r) # Calling Recursively on Right Subarray
            merge(arr,l,m,r)     # Merging Left And Right Subarray
            return           # Returning Merged Array
	
        def merge(arr:list[int],L:int,M:int,R:int) -> list[int]: 

            left          = arr[L:M+1]     # Left Subarray from L to M 
            right         = arr[M+1:R+1]   # Right Subarray From M+1 to R
            A   : int     = L              # Pointer For Arr
            i,j    = 0,0            # Pointers For Left and Right Subarray
            while i<len(left) and j<len(right):
                if left[i]< right[j]: # If Left Element Is Smaller
                    arr[A]=left[i]
                    i+=1
                    A+=1
                else:                 # Else Right Element Is Smaller
                    arr[A]= right[j]
                    j+=1
                    A+=1

            # After Loop Breaks i.e One Subarray Goes Out Of Bounds

            while i<len(left):        # If Left Has Elements Remaining
                arr[A]= left[i]
                i+=1
                A+=1

            while j<len(right):       # If Right Has Elements Remaining
                arr[A]= right[j]
                j+=1
                A+=1  
        l=0
        r=len(nums)
        mergeSort(nums,l,r)
        return nums
        