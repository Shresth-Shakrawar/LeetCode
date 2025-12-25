    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0
        decr = 0
        while k>0:
                res += h
                k -=1
            h =  happiness.pop() - decr
            if h > 0:
                decr += 1
            else:
                break
        return res