class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        array = [0] * len(nums)
        array[0] = nums[0]

        for i in range(1, len(nums)):
            array[i] = max(nums[i] + array[i-1], nums[i])
        
        return max(array)