class Solution:
    def rob(self, nums: List[int]) -> int:
        amount = [-1 for i in range(len(nums))]
        amount[0] = nums[0]
        print(amount)

        for i in range(1, len(nums)):
            amount[i] = max(amount[i-1], nums[i] + amount[i-2])

        return amount[len(nums) - 1]