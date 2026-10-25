class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # At each item, you can either subtract or add something
        # So we are kind of making a tree, with us adding/subtracting
        # from the previous item, until we read the end of nums
        # to get target
        result = [defaultdict(int) for _ in range(n + 1)]

        # At no num in nums, there is one way to get 0
        # we do nothing 
        result[0][0] = 1

        for i in range(1, n + 1):
            for num, count in result[i - 1].items():
                result[i][num - nums[i - 1]] += count
                result[i][num + nums[i - 1]] += count

        return result[n][target]

        