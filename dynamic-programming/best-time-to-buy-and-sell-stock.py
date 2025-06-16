class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice=prices[0]

        for i in range(1,len(prices)):
            maxProfit = max( (prices[i]-minPrice), maxProfit)
            minPrice = min(prices[i],minPrice)
        
        return maxProfit