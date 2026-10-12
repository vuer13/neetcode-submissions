class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROW = len(grid)
        COLUMN = len(grid[0])

        treasure = deque()
        visit = set()

        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == 0:
                    treasure.append((i, j))
                    visit.add((i, j))
        
        count = 1
        while treasure:
            len_treasure = len(treasure)
            for _ in range(len_treasure):
                i, j = treasure.popleft()
                for dx, dy in DIRECTIONS:
                    x, y = i + dx, j + dy
                    if (
                        x < 0
                        or y < 0
                        or x == ROW
                        or y == COLUMN
                        or grid[x][y] == -1
                        or (x, y) in visit
                    ):
                        continue
                    grid[x][y] = count
                    treasure.append((x, y))
                    visit.add((x, y))
            count += 1
