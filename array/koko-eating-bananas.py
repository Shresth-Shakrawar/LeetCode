class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r =  max(piles)
        l=1
        res = 0
        while l<= r:
            mid = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/mid)
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            print(f"for {mid=} {hours=} {res=}")

        return res