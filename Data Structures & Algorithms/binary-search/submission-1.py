class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = n // 2

        if n == 1 and nums[mid] != target:
            return -1

        print(mid)
        print(nums[mid])
        
        if nums[mid] == target:
            return mid

        if target > nums[mid]:
            return self.search(nums[mid:], target)
        else:
            return self.search(nums[:mid], target)
        