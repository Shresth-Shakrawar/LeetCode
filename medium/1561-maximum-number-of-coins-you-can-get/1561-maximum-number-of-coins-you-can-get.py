class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        cnt = 0
        piles.sort()
        while piles:
            piles.pop(-1) # Alice
            cnt += piles.pop(-1) #me
            piles.pop(0) #bob
        return cnt