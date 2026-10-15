class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u, v, t in times:
            adj_list[u].append((v, t))

        visited = set()
        heap = []
        t = 0

        heapq.heappush(heap, (0, k))

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = time

            for new_node, new_time in adj_list[node]:
                if new_node not in visited:
                    heapq.heappush(heap, (new_time + time, new_node))

        return t if len(visited) == n else -1
            