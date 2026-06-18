class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        l, r = 0, 1

        while len(prices) > r:
            profit = prices[r] - prices[l]
            if profit > maxSoFar:
                maxSoFar = profit
            if profit < 0:
                l = r
                r += 1
            else:
                r += 1

        return maxSoFar