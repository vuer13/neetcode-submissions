class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for x, y, t in times:
            adj_list[x].append((y, t))

        min_heap = []
        visited = set()

        time = 0
        heapq.heappush(min_heap, (0, k)) # Time 0, node k

        while min_heap:
            new_time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            time = new_time

            for next_node, next_time in adj_list[node]:
                if next_node not in visited:
                    heapq.heappush(min_heap, (time + next_time, next_node))

        return time if len(visited) == n else -1