class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        adj_list = defaultdict(list)
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

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