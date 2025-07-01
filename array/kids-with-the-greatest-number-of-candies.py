class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = []
        for c in candies:
            if c + extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res