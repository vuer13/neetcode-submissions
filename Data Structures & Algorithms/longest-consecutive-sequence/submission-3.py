class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longestLength = 0

        for n in setNums:
            if (n - 1) not in setNums:
                length = 1
                while (n + length) in setNums:
                    length += 1
                longestLength = max(length, longestLength)

        return longestLength