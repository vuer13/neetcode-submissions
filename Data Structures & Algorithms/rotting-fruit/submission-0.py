class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        queue = collections.deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        time = 0
        while queue and fresh > 0:
            lenQ = len(queue)
            for i in range(lenQ):
                r, s = queue.popleft()
                for dx, dy in directions:
                    x, y = dx + r, dy + s
                    if (
                        x < 0 or y < 0 or x >= m or 
                        y >= n or grid[x][y] == 0
                        or grid[x][y] == 2
                    ):
                        continue
                    grid[x][y] = 2
                    queue.append((x, y))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1