class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        lenNums = len(nums)
        for i in range(lenNums):
            difference = target - nums[i]
            if difference in remainders:
                return [remainders.get(difference), i]
            remainders[nums[i]] = i
            
        return None