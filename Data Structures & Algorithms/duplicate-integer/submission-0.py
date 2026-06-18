class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = nums
        for i, n in enumerate(nums):
            temp.pop(i)
            if n in temp:
                return True
            temp.insert(i, n)
        
        return False