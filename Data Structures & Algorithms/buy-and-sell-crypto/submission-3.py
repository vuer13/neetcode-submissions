class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        left, right = 0, 1

        while right != len(prices):
            profit = prices[right] - prices[left]
            if maxSoFar < profit:
                maxSoFar = profit
            if profit < 0 :
                left = right
            right += 1
        
        return maxSoFar