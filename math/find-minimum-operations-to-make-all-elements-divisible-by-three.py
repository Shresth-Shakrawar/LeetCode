class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for n in nums:
            if n % 3 == 0:
                continue
            else:
                operations += 1
        return operations