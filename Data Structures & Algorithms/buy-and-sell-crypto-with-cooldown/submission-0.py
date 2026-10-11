class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold_stock = [0] * n        # You have a stock currently (can sell or hold)
        no_hold_stock = [0] * n     # You don't have a stock currently (can buy or hold)

        if n == 1:
            return 0

        hold_stock[0] = - prices[0]
        no_hold_stock[0] = 0

        hold_stock[1] = max(no_hold_stock[0] - prices[1], hold_stock[0])
        no_hold_stock[1] = max(hold_stock[0] + prices[1], no_hold_stock[0])

        for i in range(2, n):
            no_hold_stock[i] = max(no_hold_stock[i - 1], hold_stock[i - 1] + prices[i])
            hold_stock[i] = max(hold_stock[i - 1], no_hold_stock[i - 2] - prices[i])
        
        return max(hold_stock[n - 1], no_hold_stock[n - 1])