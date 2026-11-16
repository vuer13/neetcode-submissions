class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST Problem
        # Prim's algorithm since its a dense graph
        
        n = len(points)
        adj_matrix = {i : [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj_matrix[i].append((j, dist))
                adj_matrix[j].append((i, dist))

        min_heap = []
        heapq.heappush(min_heap, (0, 0))
        visited = set()
        cost = 0
        while min_heap:
            distance, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            visited.add(point)
            cost += distance

            for next_point, next_dist in adj_matrix[point]:
                if next_point not in visited:
                    heapq.heappush(min_heap, (next_dist, next_point))

        return cost
        