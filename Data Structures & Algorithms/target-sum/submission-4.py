class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # We need to keep track of all possible sums, and after going through all nums
        # find the number of combinations

        n = len(nums)
        targets = {i : defaultdict(int) for i in range(n + 1)}
        targets[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]
            for total, count in targets[i - 1].items():
                targets[i][total + num] += count
                targets[i][total - num] += count

        return targets[n][target]
