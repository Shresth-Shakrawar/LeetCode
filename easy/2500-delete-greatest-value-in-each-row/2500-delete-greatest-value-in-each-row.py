from heapq import heapify_max,heappop_max
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
                heapify_max(grid[r])
        #print(f"{grid=}")
        while cols > 0:
            numSet= set()
            for r in range(rows):
                x = heappop_max(grid[r])
                numSet.add(x)
            res += max(numSet)
            cols -= 1
        #print(f"{res=}")
        return res
        