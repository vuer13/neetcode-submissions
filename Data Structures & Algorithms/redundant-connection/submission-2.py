class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj_list = defaultdict(list)
        in_degrees = [0] * (n + 1)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
            in_degrees[x] += 1
            in_degrees[y] += 1

        queue = deque()
        for node, degree in enumerate(in_degrees):
            if degree == 1:
                queue.append(node)

        while queue:
            node = queue.popleft()
            in_degrees[node] -= 1

            for next_node in adj_list[node]:
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 1:
                    queue.append(next_node)

        for u, v in reversed(edges):
            if in_degrees[u] > 0 and in_degrees[v] > 0:
                return [u, v]

        return []
