class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        product = 1
        sumation = 0
        for ch in string:
            n = int(ch)
            product *= n
            sumation += n

        return product - sumation