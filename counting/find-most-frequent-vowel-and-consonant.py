from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        alphaCount = Counter(s)
        sortedCount = sorted(alphaCount.items(),key = lambda x : x[1],reverse = True)
        res = 0
        vowels = ["a","e","i","o","u"]
        for key,val in sortedCount:
            if key in vowels:
                res = res + val
                break
        for key,val in sortedCount:
            if key not in vowels:
                res = res + val
                break
        return res
