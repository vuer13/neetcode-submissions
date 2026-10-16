class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COLUMN = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        fresh_fruits = 0
        queue = deque()

        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        time = 0
        while fresh_fruits > 0 and queue:
            lenQ = len(queue)
            for _ in range(lenQ):
                i, j = queue.popleft()
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if (
                        x < 0 
                        or y < 0
                        or x == ROW
                        or y == COLUMN
                        or grid[x][y] == 2
                        or grid[x][y] == 0
                    ):
                        continue
                    grid[x][y] = 2
                    queue.append((x, y))
                    fresh_fruits -= 1
            time += 1

        return time if fresh_fruits == 0 else -1