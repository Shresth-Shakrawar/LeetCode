class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        l , r = 0 , k - 1
        while r < len(arr) - 1:
            if abs(arr[r+1] - x) < abs(arr[l] - x) :
                l += 1
                r += 1
            elif arr[r+1] == arr[l]:
                l +=1
                r +=1
            else:
                break
        return arr[l:r+1]