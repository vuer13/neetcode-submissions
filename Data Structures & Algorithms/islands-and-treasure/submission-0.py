class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        visit = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            if (i < 0 
                or j < 0
                or i >= m
                or j >= n
                or (i, j) in visit
                or grid[i][j] == -1
            ):
                return

            queue.append([i, j])
            visit.add((i, j))            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visit.add((i, j))
        
        dist = 0
        while queue:
            for t in range(len(queue)):
                i, j = queue.popleft()
                grid[i][j] = dist
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    bfs(x, y)
            dist += 1