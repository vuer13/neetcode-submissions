class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        result = [defaultdict(int) for _ in range(n + 1)]
        result[0][0] = 1

        for i in range(1, n + 1):
            # From 0 to i - 1, what possible combinations do we have
            # when we add nums[i]
            num = nums[i - 1]
            for total, count in result[i - 1].items():
                result[i][total - num] += count
                result[i][total + num] += count

        return result[n][target]
