class Solution:
    def rob(self, nums: List[int]) -> int:    
        # We need to figure out the maximum amount we can "rob"
        # Restriction: we cannot rob the adjacent houses if we rob ith house

        # Assumptions:
        # 1. all numbers are valid integers
        # 2. doesn't really matter value i guess
        
        # How can we figure this out
        # Brute Force:
        # Go through every possible combination that we can get
        # Issue: exponential time

        # Examples:
        # [] => 0
        # [1] => 1
        # [1, 2] => 2 (rob second house)
        # [2, 1] => 2 (rob first house)
        # [1, 3, 1] => 3 (rob second house)
        # [1, 0, 1] => 2 (rob first and second house)
        # [1, 1, 1] => 2 
        # [1, 1, 0] => 1 (rob first OR second house)
        # [1, 0, 1, 0] => 2 (rob first and third house)
        # [1, 1, 0, 0] => 1 (rob first OR second house)
        # [0, 0, 1, 1] => 2 (rob third or fourth house)
        # [1, 0, 0, 1] => 2 (rob first and fourth house)
        # [0, 1, 1, 0] => 1 (rob second or third house)
        # Observations:
        # We cannot rob adjacent houses (clearly)
        # We don't necessarily have to rob every other house, we can skip 2 consecutive houses in a row
        # - makes me think it ISN'T GREEDY
        # What we need to know is the maximum amount 2 houses before + current amount and last house
        # this tells use what to do

        # Dynamic Programming
        # amount[i] = max(amount[i - 2] + nums[i], amount[i - 1])
        # Each spot tells us the maximum amount we rob
        # We either at minimum skip the last house (could be more) and rob this house
        # or we can just not rob this house, take the previous amount

        n = len(nums)
        amount = [0] * n

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        amount[0] = nums[0]
        amount[1] = max(nums[0], nums[1])
        for i in range(2, n):
            amount[i] = max(amount[i - 2] + nums[i], amount[i - 1])

        return amount[n - 1]
