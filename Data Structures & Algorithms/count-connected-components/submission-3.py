class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count