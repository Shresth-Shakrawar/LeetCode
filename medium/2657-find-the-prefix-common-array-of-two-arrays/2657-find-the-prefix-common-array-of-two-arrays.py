        for i in range(n):
            aSet.add(A[i])
            bSet.add(B[i])
        C = [0] * n
        c = 0
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aSet = set()
        bSet = set()
        n = len(A)
        seen = set()