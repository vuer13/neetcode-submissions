class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in hashmap:
                return [hashmap.get(remainder), i]
            else:
                hashmap[num] = i
        
        