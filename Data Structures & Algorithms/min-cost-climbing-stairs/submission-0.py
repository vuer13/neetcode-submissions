class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        array = [-1] * (len(cost) + 1)
        array[0] = 0
        array[1] = 0

        for i in range(2, len(cost) + 1):
            array[i] = min(cost[i-1] + array[i-1], cost[i-2] + array[i-2])

        return array[len(cost)]