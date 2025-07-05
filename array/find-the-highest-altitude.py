class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        res = 0
        for g in gain:
            altitude += g
            res = max(altitude,res)
        return res