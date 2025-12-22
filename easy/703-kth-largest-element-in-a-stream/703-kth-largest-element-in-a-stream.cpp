import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # min-heap
        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        return self.heap[0]  # smallest in heap = kth largest