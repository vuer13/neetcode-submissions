class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        n = len(nums)

        # m is subset allowable to be used
        # n is the target sum
        can_subset = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            can_subset[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    can_subset[i][j] = can_subset[i - 1][j] or can_subset[i - 1][j - nums[i - 1]]
                else:
                    can_subset[i][j] = can_subset[i - 1][j]
        
        return can_subset[n][target]
