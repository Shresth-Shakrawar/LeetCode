from heapq import heapify_max,heappop_max,heappush_max
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt  = Counter(tasks)
        maxHeap = [c for c in cnt.values()]
        heapify_max(maxHeap)
        time = 0
        q = deque()
        while q or maxHeap:
            time += 1
            if maxHeap :
                cnt = heappop_max(maxHeap) - 1
                if cnt != 0:
                    q.append((cnt,time+n))
            else:
                time = q[0][1]
            if q and q[0][1] == time:
                cooledDownCount = q.popleft()[0]
                heappush_max(maxHeap,cooledDownCount)
        return time
                