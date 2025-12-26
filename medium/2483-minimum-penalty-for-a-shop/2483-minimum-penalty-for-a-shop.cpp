class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = 0
        bestTime = 0
        minPenalty =0 
        for i,ch in enumerate(customers):
            prefix += -1 if ch =="Y" else 1
            if prefix < minPenalty:    
                bestTime = i+1
                minPenalty = prefix
        return bestTime