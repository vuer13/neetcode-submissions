class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST Problem
        # Will need Prim's algorithm
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
        cost = 0

        heapq.heappush(min_heap, (0, 0))

        while len(visited) < n:
            distance, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            cost += distance
            visited.add(node)

            for new_node, new_dist in adj_matrix[node]:
                if new_node not in visited:
                    heapq.heappush(min_heap, (new_dist, new_node))

        return cost
