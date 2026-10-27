class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        result = [defaultdict(int) for _ in range(n + 1)]
        result[0][0] = 1

        for i in range(1, n + 1):
            for index, count in result[i - 1].items():
                num = nums[i - 1]
                result[i][index - num] += count
                result[i][index + num] += count

        return result[n][target]
        