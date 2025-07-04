class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        sMap = {}
        tMap = {}
        charSet = set(s)
        diff = 0
        for i,c in enumerate(s):
            sMap[c] = i
        for i,c in enumerate(t):
            tMap[c] = i
        for ch in charSet:
            diff = diff + abs(sMap[ch]-tMap[ch])
        return diff