class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            s = n
            for p in piles:
                s += (p - 1) // mid
            if s <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left