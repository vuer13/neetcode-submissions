class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for x, y in points:
            dist = -((x ** 2 + y ** 2) ** 0.5)
            heapq.heappush(min_heap, (dist, x, y))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        for _, x, y in min_heap:
            result.append([x, y])

        return result
