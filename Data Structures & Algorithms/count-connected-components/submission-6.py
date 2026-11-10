class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # We need to find the number of components in an undirected graph
        # Assumptions
        # 1. all nodes are labelled 0 to n-1 for n nodes
        # 2. Edges contain numbers only b/t 0 and n-1
        # 3. There can only be up to n different components

        # Ways to do this
        # 1. Some sort of union to unionize each edge
        # 2. Some DFS to go through each edge

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
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count