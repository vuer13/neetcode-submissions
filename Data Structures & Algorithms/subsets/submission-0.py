class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bt(start, array):
            result.append(array.copy())

            for i in range(start, len(nums)):
                array.append(nums[i])
                bt(i + 1, array)
                array.pop()

        bt(0, [])
        return result