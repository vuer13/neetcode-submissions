class Solution:
    def rob(self, nums: List[int]) -> int:
        amount = [-1 for i in range(len(nums))]
        amount[0] = nums[0]
        if len(nums) == 0:
            return amount[0]
        amount[1] = max(amount[0], nums[1])

        for i in range(2, len(nums)):
            amount[i] = max(amount[i-1], nums[i] + amount[i-2])

        return amount[len(nums) - 1]