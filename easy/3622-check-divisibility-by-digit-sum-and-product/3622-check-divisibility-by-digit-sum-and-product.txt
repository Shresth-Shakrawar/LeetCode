class Solution:
    def checkDivisibility(self, n: int) -> bool:
        result = n
        Sum = 0
        Mul = 1
        while result:
            Sum += result % 10
            Mul *= result % 10 
            result //= 10
        return n % (Sum + Mul) == 0