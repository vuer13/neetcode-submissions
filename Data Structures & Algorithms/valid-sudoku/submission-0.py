class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                spot = board[r][c]
                if spot == '.':
                    continue
                if (
                    spot in rows[r]
                    or spot in cols[c]
                    or spot in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(spot)
                cols[c].add(spot)
                squares[(r // 3, c // 3)].add(spot)

        return True