class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 # l=buy sell r=sell day
        maxP=0
        while r<len(prices):
            #If profit can be made
            if prices[l] < prices[r]:
                profit= prices[r] - prices[l]
                maxP= max(profit,maxP) 
            
            # If there is a lower buying price
            elif prices[l] > prices[r]:
                l=r
            r+=1
        return maxP
        