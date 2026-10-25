class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))

    def robHelper(self, nums):
        n = len(nums)
        total = [0] * n

        if n == 1:
            return nums[0]

        total[0] = nums[0]
        total[1] = max(nums[0], nums[1])

        for i in range(2, n):
            total[i] = max(total[i - 2] + nums[i], total[i - 1])

        return total[n - 1]