class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longestLength = 0

        for num in setNums:
            if (num - 1) not in setNums:
                length = 1
                while (num + length) in setNums:
                    length += 1
                longestLength = max(length, longestLength)

        return longestLength