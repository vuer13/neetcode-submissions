class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COLUMN = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rotton_fruits = deque()
        fresh_fruits = 0

        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                if grid[i][j] == 2:
                    rotton_fruits.append((i, j))

        time = 0
        while rotton_fruits and fresh_fruits > 0:
            lenQ = len(rotton_fruits)
            for _ in range(lenQ):
                i, j = rotton_fruits.popleft()
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if (
                        x < 0
                        or y < 0
                        or x == ROW
                        or y == COLUMN
                        or grid[x][y] == 0
                        or grid[x][y] == 2
                    ):
                        continue
                    rotton_fruits.append((x, y))
                    fresh_fruits -= 1
                    grid[x][y] = 2
            time += 1

        return time if fresh_fruits == 0 else -1