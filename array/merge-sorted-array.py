class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Three Pointers Required
        i=len(nums1)-1#Points to Final Element in num1
        #m,n already given
        m,n=m-1,n-1 #Now, they Point To Largest Valid Element
        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[i]=nums1[m]
                m-=1
                i-=1
            elif nums2[n]>nums1[m]:
                nums1[i]=nums2[n]
                n-=1
                i-=1
            else:
                nums1[i]=nums2[n]
                n-=1
                i-=1
        
        while m>=0:
            nums1[i]=nums1[m]
            m-=1
            i-=1
        while n>=0:
            nums1[i]=nums2[n]
            n-=1
            i-=1


        
        