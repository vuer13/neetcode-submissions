class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # amount = 0, coins = [1, 2, 3] => 1
        # Don't use any coins
        # amount = 1, coins = [1, 2, 3] => 1
        # 1
        # amount = 2, coins = [1, 2, 3] => 2
        # 1, 1; 2
        # amount = 3, coins = [1, 2, 3] => 3
        # 1, 1, 1; 2, 1; 3
        # amount = 4, coins = [1, 2, 3] => 4
        # 1, 1, 1, 1; 2, 1, 1; 2, 2; 3, 1
        # amount = 5, coins = [1, 2, 3] => 5
        # 1, 1, 1, 1, 1; 2, 1, 1, 1; 2, 2, 1; 3, 1, 1; 3, 2

        # Dynamic Programming
        # 2-d array: amount x len(coins)
        # Each square represents the possible number of combinations for 
        # amount i using the first j coins

        # What can we do when we add a new coin to look at amount?
        # We can either:
        # 1. not use the coin (the j - 1 number of combinations)
        # 2. use that coin (look at the i - coins[j] number of combinations)

        n = len(coins)
        a = amount

        combinations = [[0 for _ in range(n)] for _ in range(a + 1)]

        # amount = 0, we don't use any coins, so we always have one possible combination
        for j in range(n):
            combinations[0][j] = 1
        # Using the first coin, it is one combination if it amount i in divisible by coin[0]
        for i in range(1, a + 1):
            combinations[i][0] = 1 if i % coins[0] == 0 else 0

        for i in range(1, a + 1):
            for j in range(1, n):
                combinations[i][j] += combinations[i][j - 1]
                if i - coins[j] >= 0:
                    combinations[i][j] += combinations[i - coins[j]][j]

        return combinations[a][n - 1]
