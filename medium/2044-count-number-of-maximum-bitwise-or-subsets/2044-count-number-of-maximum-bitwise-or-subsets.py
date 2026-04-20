        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            # Case 1: Include the current element in the subset
            include = backtrack(index + 1, current_or | nums[index])
        # Step 2: Helper function to recursively explore subsets and count those with max OR
        
            max_or |= num
        for num in nums:
        max_or = 0
        # Step 1: Find the maximum possible bitwise OR of the entire array
    def countMaxOrSubsets(self, nums: List[int]) -> int: