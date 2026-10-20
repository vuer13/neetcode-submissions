class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n 