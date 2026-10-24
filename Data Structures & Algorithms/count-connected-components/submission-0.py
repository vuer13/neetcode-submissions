class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = [False] * n

        def dfs(node):
            nonlocal seen
            seen[node] = True

            for neighbour in adj_list[node]:
                if not seen[neighbour]:
                    dfs(neighbour)
        
        result = 0
        for node in range(n):
            if not seen[node]:
                dfs(node)
                result += 1

        return result