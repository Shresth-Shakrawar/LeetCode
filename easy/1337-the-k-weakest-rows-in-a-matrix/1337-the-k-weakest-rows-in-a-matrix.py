            strength = sum(row)
            heapq.heappush_max(heap, (strength, i))  # imaginary
            if len(heap) > k:
                heapq.heappop_max(heap)
        for i, row in enumerate(mat):
        heap = []
        # weakest rows → smallest strength
        return [i for strength, i in sorted(heap)]