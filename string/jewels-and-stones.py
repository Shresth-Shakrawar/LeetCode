class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for j_ch in jewels:
            for s_ch in stones:
                if j_ch == s_ch:
                    res += 1
        return res