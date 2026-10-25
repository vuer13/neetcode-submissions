class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 4 options
        # You own stock:
        # - can sell the stock, but not buy the next day
        # - you can hold the stock
        # You don't own stock:
        # - you can buy stock, as long as it's been one day
        # - you can not own stock

        n = len(prices)

        if n == 1:
            return 0

        hold_stock = [0] * n
        no_hold_stock = [0] * n

        hold_stock[0] = -prices[0]
        hold_stock[1] = max(no_hold_stock[0] - prices[1], hold_stock[0])
        no_hold_stock[1] = max(no_hold_stock[0], hold_stock[0] + prices[1])

        for i in range(2, n):
            hold_stock[i] = max(no_hold_stock[i - 2] - prices[i], hold_stock[i - 1])
            no_hold_stock[i] = max(no_hold_stock[i - 1], hold_stock[i - 1] + prices[i])

        return max(hold_stock[n - 1], no_hold_stock[n - 1])
