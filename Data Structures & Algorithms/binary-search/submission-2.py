class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.find_index(nums, target, 0, len(nums) - 1)

    def find_index(self, nums, target, first, last):
        mid = ((last - first) // 2) + first

        print(first, last)

        if first > last:
            return -1
        
        if nums[mid] == target:
            return mid

        if target > nums[mid]:
            return self.find_index(nums, target, mid + 1, last)
        else:
            return self.find_index(nums, target, 0, mid - 1)
        