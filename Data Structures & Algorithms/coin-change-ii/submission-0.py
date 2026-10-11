class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        a = amount
        combinations = [[0 for _ in range(n)] for _ in range(a + 1)]

        for i in range(1, a + 1):
            combinations[i][0] = 1 if i % coins[0] == 0 else 0
        for j in range(n):
            combinations[0][j] = 1

        for i in range(1, a + 1):
            for j in range(1, n):
                if j > 0:
                    combinations[i][j] += combinations[i][j - 1]
                coin = coins[j]
                if i - coin >= 0:
                    combinations[i][j] += combinations[i - coin][j]
        
        return combinations[a][n - 1]