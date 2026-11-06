class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj_list = defaultdict(list)
        in_degrees = [0] * (n + 1)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
            in_degrees[i] += 1
            in_degrees[j] += 1

        queue = deque()
        for i, degree in enumerate(in_degrees):
            if degree == 1:
                queue.append(i)

        while queue:
            node = queue.popleft()
            in_degrees[node] -= 1
            
            for neighbour in adj_list[node]:
                in_degrees[neighbour] -= 1
                if in_degrees[neighbour] == 1:
                    queue.append(neighbour)

        for u, v in reversed(edges):
            if in_degrees[u] > 0 and in_degrees[v] > 0:
                return [u, v]

        return []
