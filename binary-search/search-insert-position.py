class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while True:
            mid = (l + r) // 2
            if target < nums[l]:
                return l
            elif target > nums[r]:
                return r + 1
            elif target < nums[mid] :
                r = mid - 1
                continue
            elif target > nums[mid]:
                l = mid + 1
                continue
            elif target == nums[mid]:
                return mid