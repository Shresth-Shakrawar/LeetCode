class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        answer = [0] * len(nums)
        for i in range(1,len(nums)):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            rightSum[j] = rightSum[j+1] + nums[j+1]
        for k in range(len(nums)):
            answer[k] = abs(leftSum[k] - rightSum[k])
        return answer