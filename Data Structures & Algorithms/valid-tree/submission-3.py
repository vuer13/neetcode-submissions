class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # We just need to check, have we visited this node for each node I guess
        adj_list = defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

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

        queue = deque()
        visited = set()

        return dfs(0, -1) and len(visited) == n
