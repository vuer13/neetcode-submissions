class Solution:
    def findMin(self, nums: List[int]) -> int:
        # We need to find the minimum in the array somehow
        # For which it was rotated somehow

        # Examples:
        # [0] => 0
        # [0, 1] => 0
        # [1, 0] => 0

        # [0, 1, 
        #  2, 3] => 0
        # [1, 2, 
        #  3, 0] => 0
        # [2, 3, 
        #  0, 1] => 0
        # [3, 0, 
        #  1, 2] => 0

        # Observation:
        # 1. nums[m] > nums[r]: m = l + 1
        # 2. otherwise: m = r

        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if nums[m] > nums[r]: 
                l = m + 1
            else: 
                r = m

        return nums[l]
