class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # We are going to need to find the shortest path from
        # the source k to all other nodes
        # Dijkstra's Algorithm solves this for us

        # Assumptions:
        # k exists in times
        # times is a valid graph
        # all ti in times are >0
        # nodes are labelled 1-n

        # How to implement:
        # 1. Create an adjacency list x : (y, t)
        # 2. We can start at node k (length 0)
        # 3. We need some sort of way to keep track of time and node
        # - use a minimum heap sorted by time
        # - this must be time from SOURCE NODE

        adj_list = defaultdict(list)
        for x, y, t in times:
            adj_list[x].append((y, t))
        
        min_heap = []
        heapq.heappush(min_heap, (0, k)) # Sort by time, starting from k
        visited = set()

        time = 0
        while min_heap:
            n_time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            time = n_time

            for next_node, next_time in adj_list[node]:
                if next_node not in visited:
                    heapq.heappush(min_heap, (time + next_time, next_node))

        return time if len(visited) == n else -1
