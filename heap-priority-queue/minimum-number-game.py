class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort()
        arr = []
        while nums:
            alice = nums.pop(0)
            bob = nums.pop(0)
            arr.append(bob)
            arr.append(alice)
        return arr