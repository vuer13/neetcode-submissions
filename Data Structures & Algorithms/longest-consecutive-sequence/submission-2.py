class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longest_length = 0

        for n in setNums:
            if (n - 1) not in setNums:
                length = 1
                while (n + length) in setNums:
                    length += 1
                longest_length = max(length, longest_length)

        return longest_length