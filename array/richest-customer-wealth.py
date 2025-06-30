class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for man in accounts:
            wealth = 0
            for bank in man:
                wealth += bank
            maxWealth = max(maxWealth, wealth)
        return maxWealth