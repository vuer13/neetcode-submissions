class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [amount + 1] * (amount + 1)
        result[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    result[i] = min(result[i], 1 + result[i - c])
            
        return result[amount] if result[amount] != amount + 1 else -1