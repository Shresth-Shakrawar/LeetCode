class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for n in arr1:
            prefixes.add(n)
            while n // 10 > 0:
                n= n // 10
                prefixes.add(n)
        res =0