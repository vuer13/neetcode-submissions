class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(array):
            if len(array) == len(nums):
                result.append(array.copy())
                return
                
            for num in nums:
                if num in array:
                    continue
                array.append(num)
                bt(array)
                array.pop()

        bt([])
        return result