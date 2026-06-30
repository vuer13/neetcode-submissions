class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        lenNums = len(nums)
        for i in range(lenNums):
            currNum = nums[i]
            difference = target - currNum
            if difference in remainders:
                smallerIndex = remainders.get(difference)
                return [smallerIndex, i]
            remainders[currNum] = i
            
        return None