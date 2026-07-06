class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMax = 1
        currMin = 1

        for n in nums:
            tempMax = currMax * n
            tempMin = currMin * n
            currMax = max(tempMax, tempMin, n)
            currMin = min(tempMax, tempMin, n)
            result = max(currMax, result)

        return result