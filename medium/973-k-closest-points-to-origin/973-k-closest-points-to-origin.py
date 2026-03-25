from heapq import heapify_max,heappush_max,heappop_max
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify_max(heap)
        for p in points:
            x,y = p # unpack point
            dist = math.sqrt(abs(x)**2+abs(y)**2)
            heappush_max(heap,(dist,x,y))
            #print(f"After Pushing {heap=}")
            if len(heap) > k:
                heappop_max(heap)
        res = []
        for tup in heap:
            dist,x,y = tup
            res.append([x,y])
        return res