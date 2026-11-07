class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 4 options
        # Buy and sell a stock
        # Sell a stock, cannot buy for one day
        # Hold at most one coin
        # We can hold one stock, or no stocks
        # 1. Buy a stock (not holding one previously)
        # 2. Hold a stock (don't buy or sell)
        # 3. Sell a stock (held one previously, cannot buy for another day)
        # 4. Not hold a stock (don't buy or sell)
        # [0] => 0 b/c you can buy it or not do anything
        # [1] => 0 b/c you can not do anything (if you buy, profit is -1)
        # [0, 0] => 0 b/c you can do any of the combinations above
        # [0, 1] => 1 b/c you can buy at 0, sell at 1
        # [1, 0] => 0 b/c you can just not do anything (or buy at 0)
        # [1, 1] => 0 b/c you buy and sell (or do nothing)
        # [0, 1, 2] => 2 b/c you can buy at 0, sell at 2
        # [1,3,4,0,4] => 6 b/c you can buy at day 0, sell at day 1, buy day 3 
        # (skip day 2), sell at day 4

        n = len(prices)

        if n == 1:
            return 0

        hold_stock = [0] * n
        no_hold_stock = [0] * n

        # Intialization
        hold_stock[0] = -prices[0] # You bought a stock 
        hold_stock[1] = max(-prices[1], hold_stock[0])
        no_hold_stock[1] = max(no_hold_stock[1], hold_stock[0] + prices[1])

        for i in range(2, n):
            hold_stock[i] = max(hold_stock[i - 1], no_hold_stock[i - 2] - prices[i])
            no_hold_stock[i] = max(no_hold_stock[i - 1], hold_stock[i - 1] + prices[i])

        return max(hold_stock[n - 1], no_hold_stock[n - 1])
