class Solution:
    def rob(self, nums: List[int]) -> int:    
        if len(nums) == 1:
            return nums[0]

        lenNums = len(nums)
        
        amount = [-1] * lenNums

        amount[0] = nums[0]
        amount[1] = max(amount[0], nums[1])

        for i in range(2, lenNums):
            amount[i] = max(amount[i-1], nums[i] + amount[i-2])

        return amount[lenNums - 1]