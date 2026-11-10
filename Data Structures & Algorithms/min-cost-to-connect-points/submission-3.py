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
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_matrix[i].append((j, dist))
                adj_matrix[j].append((i, dist))

        min_heap = []
        visited = set()

        heapq.heappush(min_heap, (0, 0))        # Start at point 0
        min_dist = 0
        while min_heap:
            distance, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            min_dist += distance

            for next_node, next_dist in adj_matrix[node]:
                if next_node not in visited:
                    heapq.heappush(min_heap, (next_dist, next_node)) 

        return min_dist
        