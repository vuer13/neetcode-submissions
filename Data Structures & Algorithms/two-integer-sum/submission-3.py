class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in remainders:
                smallerIndex = remainders.get(difference)
                return [smallerIndex, i]
            remainders[n] = i
            
        return None