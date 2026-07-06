class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [amount + 1] * (amount + 1)
        change[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    change[a] = min(1 + change[a - c], change[a])
        
        return change[amount] if change[amount] != amount + 1 else -1