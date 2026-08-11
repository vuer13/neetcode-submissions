class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []

        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(closestPoints, [dist, x, y])
            if len(closestPoints) > k:
                heapq.heappop(closestPoints)

        result = []
        for _, x, y, in closestPoints:
            result.append([x, y])

        return result