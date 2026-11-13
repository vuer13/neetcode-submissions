class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        ROW, COLUMN = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            grid[i][j] = 0

            area = 1
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    m, n = x + dx, y + dy
                    if (
                        m < 0
                        or n < 0
                        or m == ROW
                        or n == COLUMN
                        or grid[m][n] == 0
                    ):
                        continue
                    grid[m][n] = 0
                    area += 1
                    queue.append((m, n))

            return area

        maxArea = 0
        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == 1:
                    area = bfs(i, j)
                    maxArea = max(area, maxArea)

        return maxArea
        """

        ROW, COLUMN = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x, y):
            if (
                x < 0 or y < 0
                or x >= ROW or y >= COLUMN
                or grid[x][y] == 0
            ):
                return 0

            grid[x][y] = 0 
            area = 1      

            for dx, dy in DIRECTIONS:
                area += dfs(x + dx, y + dy)

            return area

        maxArea = 0
        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(area, maxArea)

        return maxArea
