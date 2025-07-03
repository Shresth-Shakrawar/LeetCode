class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        r = range(n+1)
        num1 = sum([x for x in r if x % m !=0])
        num2 = sum([x for x in r if x % m ==0])
        return num1 - num2