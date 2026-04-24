        def backtrack(r):
            if r == n :
                copy = ["".join(row) for row in board].copy()
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)
                board[r][c] = "."
        #print(f"{board=}")
        board = [["."]* n for _ in range(n)]
        res :List[List[str]]= []
        negDiag = set()
        posDiag = set()
        col = set()
    def solveNQueens(self, n: int) -> List[List[str]]:
class Solution:
                col.remove(c)