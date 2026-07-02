class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        len_cost = len(cost)

        # Initialization
        minCosts = [-1] * len_cost

        # Base Cases
        minCosts[0] = cost[0]
        minCosts[1] = cost[1]

        for c in range(2, len_cost):
            cost_c = cost[c]
            minimum = min(minCosts[c - 2], minCosts[c - 1])
            minCosts[c] = cost_c + minimum
            
        return min(minCosts[len_cost - 2], minCosts[len_cost - 1])
