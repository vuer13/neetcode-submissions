class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # We need to find a duplicate number in nums 
        # nums only contains numbers [1, n] and has size n + 1

        # Assumptions:
        # 1. All values in nums are integers, not strings
        # 2. Using index-0 
        # 3. nums is at least size 2 (based on problem statement)

        # [1, 1] => 1 since 1 is the duplicate here
        # [1, 1, 2] => 1 
        # [1, 2, 2] => 2
        # [2, 1, 2] => 2

        # Observations:
        # We need some place to "indicate" that we've seen these numbers
        # Space considerations:
        # Using a set: O(n)
        # Can we modify the array such that we've "seen" this number
        # Maybe we can set some sort of flag
        # Maybe modify the index such that its negative?

        for num in nums:
            if nums[abs(num) - 1] < 0:
                return abs(num)
            nums[abs(num) - 1] *= -1

        return -1
