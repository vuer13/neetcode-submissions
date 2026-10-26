class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for x, y, t in times:
            adj_list[x].append((y, t))

        # Dikystra's algorithm
        min_heap = []
        heapq.heappush(min_heap, (0, k))

        visited = set()
        cost = 0

        while min_heap:
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            visited.add(curr_node)
            cost = curr_cost

            for neighbour, new_cost in adj_list[curr_node]:
                if neighbour not in visited:
                    heapq.heappush(min_heap, (curr_cost + new_cost, neighbour))

        return cost if len(visited) == n else -1
            